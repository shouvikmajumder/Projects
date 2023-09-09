from bs4 import BeautifulSoup
import requests
import re

search = input("What graphics card do you want to search for? ")

url = f"https://www.newegg.com/p/pl?d={search}&N=4131"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

pages_find = doc.find(class_="list-tool-pagination-text")

lastpage = int(pages_find.strong.text.split("/")[-1])

itemsfound = {}

for page in range(1, lastpage + 1):
    url = f'https://www.newegg.com/p/pl?d={search}&page={page}'
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
    items = div.find_all(text=re.compile(search))
    link = None
    for item in items:
        parent = item.parent
        if parent.name != "a":
            continue
        link = parent["href"]
        next_parent = item.find_parent(class_="item-container")
        try:
            price = next_parent.find(class_="price-current").strong.string
        except AttributeError:
            price = "N/A"  # If price not found, set it to "N/A"

        itemsfound[item] = {"price": price, "link": link}

# The sorting function should be within the sorted function call.
sorteditems = sorted(itemsfound.items(), key=lambda x: x[1]["price"])

for item in sorteditems:
    print(item[0])
    print(f"Price: ${item[1]['price']}")
    print(f"Link: {item[1]['link']}")
