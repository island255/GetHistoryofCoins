#coding:utf-8
import csv
from bs4 import BeautifulSoup
import requests
import time
from requests.packages import urllib3

head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'}
prefix = "https://coinmarketcap.com"

csv_file = csv.reader(open('catalogue.csv', 'r'))
date = []
link = []
num = []
for line in csv_file:
    date.append(line[0])
    link.append(line[1])
# print(link)
for i in range(0, len(date)):
    url = link[i]
    print(url)
    urllib3.disable_warnings()
    r = requests.get(url, head)
    # rtimes = 0
    while (r.status_code != 200):
        time.sleep(5)
        # rtimes += 1
        r = requests.get(url, head)
    # if rtimes > 30:
    #     continue
    soup = BeautifulSoup(r.text, "html.parser")

    coinsindex = soup.find("tbody")
    coins = coinsindex.findAll("tr")
    f = open("timedata\\" + date[i] + ".csv", "w")
    num.append(str(len(coins)))

    for j in range(len(coins)):
        coin = coins[j]
        rank = coin.td.string.strip()
        name = coin.find("td", {"class": "no-wrap currency-name"}).attrs["data-sort"]
        symbol = coin.find("td", {"class": "text-left col-symbol"}).string.strip()
        Maketcap = coin.find("td", {"class": "no-wrap market-cap text-right"}).string.strip().replace(",", "")
        price = coin.find("td", {"class": "no-wrap text-right"}).a.string.strip().replace(",", "")
        supply = coin.find("td", {"class": "no-wrap text-right circulating-supply"}).span.string.strip().replace(",",
                                                                                                                 "")
        coinlink = coin.find("span", {"class": "currency-symbol visible-xs"}).a.attrs["href"]
        # print(rank+name+symbol+Maketcap+price+supply)
        f.write(
            rank + "," + name + "," + symbol + "," + Maketcap + "," + price + "," + supply + "," + prefix + coinlink + "\n")
    f.close()
    time.sleep(5)
f = open("timeandnum.csv", "w")
for i in range(len(date)):
    f.write(date[i] + "," + num[i] + "\n")
f.close()
