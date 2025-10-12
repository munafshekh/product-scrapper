import requests
from bs4 import BeautifulSoup
import json

'''
Need to install these libraries:
bs4 for BeautifulSoup
lxml (maybe not needed if you are using html parsing)
requests
'''

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive',
}


# x = requests.get('https://w3schools.com/python/demopage.htm').text
# y = requests.get('https://google.com')

try:
    url_amz = 'https://www.amazon.com/YILUSHENGHUA-Moisture-Proof-Container-Countertop-Kaleidoscope/dp/B0FPBF3GD6/ref=sr_1_1?_encoding=UTF8&sr=8-1'

    amz_data = requests.get(url_amz, headers=headers, timeout=10)
    amz_data.raise_for_status() #Checks if request was successful

    print(f"Status Code : {amz_data.status_code}")

    if amz_data.status_code == 200:
        soup = BeautifulSoup(amz_data.content, "html.parser")


        # Logic for parsing
        title = soup.find("span", {"id": "productTitle"})
        if title:
            print(f"Product Title : {title.get_text().strip()}")
        else:
            print("Product title not found")
        
    else:
        print(f"Recived status code : {amz_data.status_code}")
        print("Amazon is blocking the request")


except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")




# Parsing html content usinf beautifulsoup
# soup = BeautifulSoup(amz_data.text, "lxml")
# print(soup.prettify()) # Prints the parsed data fo html seems like you need to write this
# print("Testing git XOXO")

# print(soup.find_all("productTitle"))


# print(soup.title)
