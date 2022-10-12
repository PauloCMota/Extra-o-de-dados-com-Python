import requests
from bs4 import BeautifulSoup


res = requests.get("https://www.lotoloto.com.br/sorteios/megasena/")
res.encoding = 'utf-8'

soup = BeautifulSoup(res.text , "html.parser")
all_posts = soup.find_all(class_='numeros')
print(all_posts)
