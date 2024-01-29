import requests
from bs4 import BeautifulSoup

# HTML content containing the span element
html_content = '<span class="_ac2a _ac2b"><span class="d ">

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Select the span element with the specific class
span_element = soup.find('span', class_='html-span ')

# Extract the text from the span element
if span_element:
    number = span_element.text
    print("Number:", number)
else:
    print("Span element not found.")
