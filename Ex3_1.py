import requests
from bs4 import BeautifulSoup
page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
# print(seven_day)
forecast_items = seven_day.find_all(class_="tombstone-container")
# print(forecast_items)
tonight = forecast_items[0]
print(tonight.prettify())
period = tonight.find(class_="period-name")
desc = tonight.find(class_="short-desc")
temp = tonight.find(class_="temp")
print(period.get_text())
print(desc.get_text())
print(temp.get_text())
img = tonight.find('img')
print(img['alt'])


