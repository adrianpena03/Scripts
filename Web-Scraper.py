# Scrape information from a website:
# Start by writing a script to extract information from a website. 
# This involves basic web scraping techniques using libraries like BeautifulSoup in Python. 

# Create a BeautifulSoup object to parse the HTML
import requests
from bs4 import BeautifulSoup

# URL of the website
url = 'https://weather.com/weather/today/l/a67a051c5474a8f3ae3b51bc8245f9a813149c99a3d8a9b91013ace2e20b1efb'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # EXTRACT LINKS CODE
    links = soup.find_all('a')
    # Print the links
    for link in links:
        print(link.get('href'))
    
    # EXTRACT PARAGRAPH TEXT
    # paragraphs = soup.find_all('p')
    # print("Paragraphs:")
    # for paragraph in paragraphs:
    #         print(paragraph.get_text())

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
