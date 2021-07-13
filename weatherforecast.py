import requests
# from main import speak

api_key = "5d52a94d4dcb8a2a52599d68a44*****"  # Place Your Api Here
"""Go to openweathermap Website, register and get your own free api with 50 requests per day"""
base_url = "https://api.openweathermap.org/data/2.5/weather?"
print("Enter Your City Name")
city_name = str(input())
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)
x = response.json()
if x["cod"] != "404":
    y = x["main"]
    current_temperature = int(y["temp"] - 273.15)
    current_feelslike = int(y["feels_like"] - 273.15)
    current_humidity = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]
    print(" Current Temperature is " +
          str(current_temperature) + "Degree Celsius" +
          "\n But It Feels Like " +
          str(current_feelslike) +
          "\n humidity is " +
          str(current_humidity) + "Percent"
                                  "\n probability of " +
          str(weather_description))
    
