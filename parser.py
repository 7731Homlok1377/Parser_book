import re

import requests
from bs4 import BeautifulSoup

import config

def write_to_file(i, req):
    with open(f"page_{i}.html", "w", encoding="utf-8") as file:
        file.write(req.text)

with open("main.html", encoding="utf-8") as file:
    src = file.read()
soup = BeautifulSoup(src, "lxml")
all_category_hrefs = soup.find_all(class_ = "pagination__text")
print(all_category_hrefs[-1].text)


#https://www.chitai-gorod.ru/catalog/books-18030?page=1

for page in range(5):
    # req = requests.get(f"https://www.chitai-gorod.ru/catalog/books-18030?page={page}", headers=config.headers)
    # write_to_file(page, req)
    with open(f"page_{page}.html", encoding="utf-8") as file:
        src = file.read()
    soup_page = BeautifulSoup(src, "lxml")

    book_titles = soup_page.find_all(class_ = "product-card product-card product")
    # nn = soup_page.find_all(class_ = "product-price__value product-price__value--discount")
    # author = book_titles.get("data-chg-product-name")
    for i in book_titles:
        n = i
        author = i.find(class_ = "product-title__author")
        name = i.find(class_ = "product-title__head")
        #product-price__value
        price = i.find(class_ = "product-price__value product-price__value--discount")
        if price == None:
            price = i.find(class_="product-price__value")
        price = price.text
        price = price.replace(" ", "")
        price = re.findall(r'\d+', price)
        if len(price) > 1:
            len_p = ""
            for item in price:
                len_p = len_p + item
        else:
            len_p = price[0]
        # author = i.get("div")
        book_info = {'Nme': name}
        print(name.text, author.text, len_p)



#product-title__head
#product-title__author

# for i in all_category_hrefs:
#     print(i)
#catalog-mobile-menu__item catalog-mobile-menu__item--first-level