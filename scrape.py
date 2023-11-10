import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone, timedelta
from urllib.parse import urljoin
import json

url = 'https://www.theverge.com/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.find_all('h2', class_='font-polysans text-20 font-bold leading-100 tracking-1 md:text-24 lg:text-20')

headlines = []

for article in articles:
    title_element = article.find('a')
    title = title_element.text.strip()
    link = urljoin(url, title_element['href'])  # Convert the relative link to absolute
    pub_date_str = article.find_next('time')['datetime']

    # Parse the datetime string without the UTC offset
    pub_date = datetime.strptime(pub_date_str, '%Y-%m-%dT%H:%M:%S.%fZ')

    # Add the UTC timezone to the datetime object
    pub_date = pub_date.replace(tzinfo=timezone.utc)

    # Check if the article was published from 1st January 2022 onwards
    if pub_date >= datetime(2022, 1, 1, tzinfo=timezone.utc):
        headlines.append({"title": title, "link": link, "pub_date": pub_date.isoformat()})

# Save headlines to a JSON file
with open('headlines.json', 'w') as json_file:
    json.dump(headlines, json_file)
