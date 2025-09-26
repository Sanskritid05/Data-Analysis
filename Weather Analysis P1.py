import requests

API_KEY = 'c73d8cd3bcfa9a8a1dd6865fde40b6d6'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(cities):
    print("\n")
    for city in cities : 
        try:
            request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
            response = requests.get(request_url)
            response.raise_for_status()  # Raise error for bad status codes
            data = response.json()
    
            weather = data['weather'][0]['description']
            temperature = round(data['main']['temp'] - 273.15, 2)  # Kelvin to Celsius
    
            print(f"Weather in {city}: {weather}")
            print(f"Temperature: {temperature} °C")

        except requests.exceptions.HTTPError:
            print(f"City '{city}' not found or API request failed. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print("Error connecting to the API:", e)
        except KeyError:
            print("Unexpected response format from API.")

if __name__ == "__main__":
    
    print("__Weather Analysis__\n")
    n = int(input("Enter the number of cities/states : "))
    
    cities = [] 
    print("Enter the cities/states : ")
    for i in range(n) : 
        city = input(f"City {i+1} : ")
        # city.strip()          # doesn't work 
        cities.append(city)
        
    get_weather(cities)  