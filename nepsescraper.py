from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime, date

url="https://merolagani.com/latestmarket.aspx"
source= requests.get(url)
soup=BeautifulSoup(source.text, "lxml")

rows= soup.select("table.table tbody tr")
price_dict=[]

for row in rows:
    title_tag= row.find("a")
    title_text= title_tag.get("title")
    title_name=title_text.split("(")
    title= title_name[1].replace(")", "")
    

    symbol_tag= title_text.split("(")
    symbol= symbol_tag[0]
    


    tds=row.find_all("td")

    if len(tds)<7:
        continue

    Ltp= tds[1].text.strip()
    change= tds[2].text.strip()
    openp=tds[3].text.strip()
    high=tds[4].text.strip()
    low=tds[5].text.strip()
    qty=tds[6].text.strip()
    

    price_dict.append({"title":title, "symbol":symbol, "LTP":Ltp, "change":change, "openp":openp, "high":high, "low":low, "qty":qty})


for price in price_dict:
    print("Company name:", price['title'])
    print("Symbol:", price['symbol'])
    print("LTP:", price['LTP'])
    print("change:", price['change'])
    print("opening price:", price['openp'])
    print("high:", price['high'])
    print("low:", price['low'])
    print("quantity:", price['qty'])
    print("-"*50)


try:
    with open ("Nepse.json", "r") as f:
        all_data= json.load(f)
except FileNotFoundError:
     all_data=[]

all_data.append({"date":str(datetime.now().date()),
                 "data": price_dict
                 })   

with open ("Nepse.json", "w") as f:
        json.dump(all_data, f, indent=4)

    




