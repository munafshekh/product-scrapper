import requests
from bs4 import BeautifulSoup

x = requests.get('https://w3schools.com/python/demopage.htm').text
y = requests.get('https://google.com')
amz = requests.get('https://www.amazon.com/CyberPowerPC-i9-14900KF-GeForce-Windows-GXiVR8080A39/dp/B0DW48QHFY/ref=sr_1_6?_encoding=UTF8&content-id=amzn1.sym.fe35c7fa-b4ae-4612-b878-056854c790ff&dib=eyJ2IjoiMSJ9.Z1gXDy0H8dNKp8LlcdArdu4Sy7HdabS9dhLdFtf7DEVkWaZRk8zyBPqLLXmnAACneoaG0LCylkRhgGXDG_YuOWXCuKX7tJWvue6OEos60Dreqznjc03RLQwT7xbBKLkixROKooEi3X5bXP4kGkLXmasPzKGjvjFtFbFkGp8VlmHzlG5fY4MYZRDeDLAbYzTS9vQXOdizjEkS3deq5-flBlUH3WHYRliel5DsNVfyKpK6MG84-PdLCTLxgg7RMuzMu4z6CvfLfWZLO1FCcnPROVr-8BGqHl5LkyxFol1UN0U.f3AFXZvLYOiMdn1bKlopzc1rE6fRRIJa_yXUgnCjM3w&dib_tag=se&keywords=gaming&pd_rd_r=1cd55f62-8ea6-4224-b495-b0b774430f56&pd_rd_w=xzfIq&pd_rd_wg=Xe2zM&qid=1760005995&sr=8-6')

# print(x)

# Parsing html content usinf beautifulsoup
soup = BeautifulSoup(amz.text, "lxml")
print(soup.prettify()) # Prints the parsed data fo html seems like you need to write this
print("Testing git")
