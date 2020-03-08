import requests
from  bs4 import BeautifulSoup

PAGE_URL ='https://weather.com/weather/tenday/l/Tehran+Iran+IRXX0018'
page = requests.get(PAGE_URL)

soup = BeautifulSoup(page.content,'html.parser')
# print(soup)

weather_table = soup.find('table', attrs ={'class':'twc-table'})

# choose this class so each object of array contanis data for one day ----->> so we can use for loop
weather_content = weather_table.findAll( 'tr' ,attrs= {'class' :'clickable closed'})

#################################   important   #################################
#save data into an array of objects

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

print(result_array)