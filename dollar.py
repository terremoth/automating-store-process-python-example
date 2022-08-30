import requests
from bs4 import BeautifulSoup

def dolar_price():
    page = requests.get("https://dolarhoje.com")

    if page.status_code == 200:
        parser = BeautifulSoup(page.content, 'html.parser')
        dolar_value_str = parser.find(id='nacional').get('value')
        return float(dolar_value_str.replace(',','.'))
    
    return 5.00