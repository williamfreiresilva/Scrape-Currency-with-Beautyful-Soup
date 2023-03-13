from bs4 import BeautifulSoup
import requests

#BeautifulSoup understand HTML
in_currency = input('Enter rate you wish to convert: ')
out_currency = input('Enter rate you wish to obtain: ')
amount = input('Enter amount to be converted: ')

def get_currency(in_currency, out_currency, amount):
  url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount={amount}"
  content = requests.get(url).text
  soup = BeautifulSoup(content, 'html.parser')
  soup = soup.find("span", class_="ccOutputRslt").get_text()
  soup = soup.replace(',', '')
  soup = float(soup[:-4])
  return soup

current_rate = get_currency(in_currency,out_currency,amount)
print(current_rate)