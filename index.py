import requests
from bs4 import BeautifulSoup

# Replace 'url' with the actual URL of the website you want to scrape
url = 'https://example.com'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract information by navigating the HTML structure
    # Example: Extract all the text from paragraph elements
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        print(paragraph.text)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
 
