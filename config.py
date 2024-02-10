import requests
from bs4 import BeautifulSoup

url = "https://www.chitai-gorod.ru/catalog/books-18030"
headers = {
"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36"
}

#База данных

host = "127.0.0.1"
user = "postgres"
password = "pppp"
db_name = "Parse_Book"


#создание основной страницы

# req = requests.get(url, headers = headers)
# src = req.text
# with open("main.html", "w", encoding="utf-8") as file:
#     file.write(src)

