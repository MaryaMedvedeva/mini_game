import requests
from bs4 import BeautifulSoup

def scrape_weather():
    url = 'https://ua.sinoptik.ua/погода-лос-анджелес'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    forecast = soup.find('div', class_='main loaded')
    date = forecast.find('p', class_='day-link').text.strip()
    temperature = forecast.find('div', class_='temperature').text.strip()
    description = forecast.find('div', class_='weatherIco')['title']

    print(f"Weather on {date}:")
    print(f"Temperature: {temperature}")
    print(f"Description: {description}")

if __name__ == "__main__":
    scrape_weather()
