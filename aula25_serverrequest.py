import requests
from bs4 import BeautifulSoup


url = 'https://www.remessaonline.com.br/cotacao/cotacao-dolar'
response = requests.get(url)
parsed_html = BeautifulSoup(response.content, 'html.parser', from_encoding='utf-8')
#print(parsed_html.text)


dolar = parsed_html.select_one('#root > div:nth-child(3) > div > div.style__Container-sc-1a6mtr6-0.eLPrNc > div > div.style__Text-sc-1a6mtr6-2.ljisZu')

if dolar is not None:
    print(dolar.text)
    
    