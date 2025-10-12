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


def data_found(request, name):
    if request:
        print(f"{name}  : {request.get_text().strip()}")
    else:
        print("Not found")

def price_finder(price, fraction, name):
    if price:
        prc = float(f"{price.get_text().strip()}{fraction.get_text().strip()}")
        print(f"{name}  : £{prc}")
    else:
        print("Not found")



# x = requests.get('https://w3schools.com/python/demopage.htm').text
# y = requests.get('https://google.com')

try:
    url_amz = 'https://www.amazon.co.uk/dp/B07Q6YSGF9/ref=sspa_dk_detail_0?psc=1&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM'

    amz_data = requests.get(url_amz, headers=headers, timeout=10)
    amz_data.raise_for_status() #Checks if request was successful

    print(f"Status Code : {amz_data.status_code}")

    if amz_data.status_code == 200:
        soup = BeautifulSoup(amz_data.content, "html.parser")

        # Logic testing
        print(soup.prettify())
        

        # Product essentials
        title = soup.find("span", {"id": "productTitle"})
        data_found(title, "Product title")

        rating = soup.find("span", {"class": "a-icon-alt"})
        data_found(rating, "Rating")

        total_rating = soup.find("span", {"id":"acrCustomerReviewText"})
        data_found(total_rating, "Total Rating")

        price = soup.find("span", {"class": "a-price-whole"})
        fraction = soup.find("span", {"class": "a-price-fraction"})
        price_finder(price, fraction, "Price")
        
        last_bought = soup.find("span", {"id":"social-proofing-faceout-title-tk_bought"})
        data_found(last_bought, "Last bought")

        # Product details
        product_details = soup.find("h2", {"Product details"})
        data_found(product_details, "Product details")
        
        
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


