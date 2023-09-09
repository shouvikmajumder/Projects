from bs4 import BeautifulSoup
import requests 

url = "https://coinmarketcap.com/"

result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")

tbod = doc.tbody

trs = tbod.contents

prices = {}

for tr in trs[:10]: 
    name, price = tr.contents[2:4]
    coinnames = name.p.text
    coinprice = price.span.text
    prices[coinnames] = coinprice

print(prices)



# baselist = []
# for i in trs:
#     for stuff in i.contents[2:4]: 
#         baselist += [stuff.text]

# index = len(baselist)-1
# count = 0 
# namelst = []
# priceslst = []
# while count <= index:
#     if count %2 == 0:
#         namelst += [baselist[count]]
#         count +=1
#     elif count % 2 != 0:
#         priceslst += [baselist[count]]
#         count += 1

# newindex = len(namelst)-1
# count = 0
# while count <= newindex:
#     # print(namelst[count], priceslst[count])
#     prices[namelst[count]] =priceslst[count]
#     count += 1

# temp = min(prices.values())
# res = [key for key in prices if prices[key] == temp]

# for key in res:
#     print(prices[key])
    
# # printing result
# print("Keys with max values are : " + str(res))
# # print(f'{res}: {prices[res]}')



