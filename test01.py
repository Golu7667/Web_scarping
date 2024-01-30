import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = 'https://calculator-project-omega.vercel.app/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')


print(soup)
