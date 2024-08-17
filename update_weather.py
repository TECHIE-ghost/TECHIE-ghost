import requests
import os

def get_location():
    try:
        response = requests.get('https://ipapi.co/json/')
        data = response.json()
        return data['city'], data['latitude'], data['longitude']
    except Exception as e:
        print(f"Error getting location: {e}")
        return "Unknown", 0, 0

# Replace with your API key
API_KEY = os.environ.get('OPENWEATHERMAP_API_KEY')

# Get current location
CITY, LAT, LON = get_location()

# Use coordinates for more accurate results
url = f"http://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

temperature = data['main']['temp']
description = data['weather'][0]['description']

# Create or update the weather badge URL
badge_url = f"https://img.shields.io/badge/{CITY}-{temperature:.1f}°C%20{description}-blue"

# Update the README.md file
with open('README.md', 'r') as file:
    readme = file.read()
    # Replace the existing weather badge with the new one
    updated_readme = readme.replace(
        r'!\[Weather\].*',
        f'![Weather]({badge_url})'
    )

with open('README.md', 'w') as file:
    file.write(updated_readme)

print(f"Updated weather for {CITY}: {temperature:.1f}°C, {description}")
