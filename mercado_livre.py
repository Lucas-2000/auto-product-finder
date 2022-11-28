import requests
from bs4 import BeautifulSoup
import pandas as pd

products_list = []

base_url = 'https://lista.mercadolivre.com.br/'

product_name = input('What product you want? ')

response = requests.get(base_url + product_name)

site = BeautifulSoup(response.text, 'html.parser')

products = site.find_all('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core andes-card--padding-default'})

for product in products:
  title = product.find('h2', attrs={'class': 'ui-search-item__title'})
  link = product.find('a', attrs={'class': 'ui-search-link'})
  price = product.find('span', attrs={'class': 'price-tag-fraction'})
  cents = product.find('span', attrs={'class': 'price-tag-cents'})
  
  if cents:
    products_list.append([title.text, link['href'], price.text, cents.text])
  else:
    products_list.append([title.text, link['href'], price.text, 0])

products_df = pd.DataFrame(products_list, columns=['title', 'link', 'price', 'cents']) 

products_df.to_excel(product_name + '.xlsx', index=False)