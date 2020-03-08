import requests
from  bs4 import BeautifulSoup
import  pandas as pd

PAGE_URL ='https://weather.com/weather/tenday/l/Tehran+Iran+IRXX0018'
page = requests.get(PAGE_URL)

soup = BeautifulSoup(page.content,'html.parser')
# print(soup)

weather_table = soup.find('table', attrs ={'class':'twc-table'})

# choose this class so each object of array contanis data for one day ----->> so we can use for loop
weather_content = weather_table.findAll( 'tr' ,attrs= {'class' :'clickable closed'})

#################################   save data into an array of objects   #################################

result_array=[]
for object in weather_content:
    daily_forcast={}# save data for one day into an object
    daily_forcast['day']=object.find('span', attrs={'class': 'date-time'}).text
    #we can either use  'text' property of 'get_text()' Method
    daily_forcast['short_description'] = object.find('td', attrs={'class': 'description'}).get_text()

    # to get an attribute we can simply use 'get' funection
    daily_forcast['description'] = object.find('td', attrs= {'class' : 'description'}).get('title')
    daily_forcast['humidity'] = object.find('td', attrs={'class': 'humidity'}).get_text()
    result_array.append(daily_forcast)

############################# Save data into DataFrame using 'Panda' ##########################
#save data for each coloum into an array to use in panda
date_time_array=[]
short_desc_array=[]
long_desc_array=[]
humidity_array=[]
for object in weather_content:
    date_time_array.append(object.find('span', attrs={'class': 'date-time'}).text)
    short_desc_array.append(object.find('td', attrs={'class': 'description'}).get_text())
    long_desc_array.append(object.find('td', attrs= {'class' : 'description'}).get('title'))
    humidity_array.append(object.find('td', attrs={'class': 'humidity'}).get_text())

dictionary_for_panda ={
    'Weekday' :date_time_array,
    'Short Description': short_desc_array,
    'Long Description': long_desc_array,
    'Humidity' : humidity_array,
}

#save data into DataFrame using panda
result_dataframe = pd.DataFrame(dictionary_for_panda)
print(result_dataframe)
