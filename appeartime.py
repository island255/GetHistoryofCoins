import csv
import os
from datetime import datetime

def readcoins(filepath):
    coins=[]
    market_caps=[]
    date=[]
    links=[]
    pathdir = os.listdir(filepath)
    for allDir in pathdir:
        date.append(allDir.replace(".csv",""))
        child = os.path.join('%s\%s' % (filepath, allDir))
        # print (child)
        csv_reader = csv.reader(open(child,'r'))
        coin=[]
        market_cap=[]
        link=[]
        for line in csv_reader:
            coin.append(line[2])
            market_cap.append(line[3].replace("$",""))
            link.append(line[6])
        coins.append(coin)
        market_caps.append(market_cap)
        links.append(link)
    return coins, market_caps, date, links

def findallcoins(coins):
    allcoins=[]
    for i in range(0,len(coins)):
        allcoins= list(set(allcoins).union(set(coins[i])))
    return allcoins

def writecoinstime(deadcoins,coins,market_caps,date):
    for i in range(len(deadcoins)):
        print(deadcoins[i])
        if(deadcoins[i]=="PRN"):
            continue
        csv_writer = csv.writer(open("allcoin\\"+deadcoins[i]+".csv",'w',newline=''))
        for j in range(len(coins)):
            if deadcoins[i] in coins[j]:
                deaddate=date[j]
                deadindex= coins[j].index(deadcoins[i])
                deadmarket_cap= market_caps[j][deadindex]
                line=[]
                line.append(datetime.strptime(deaddate,'%Y%m%d'))
                line.append(deadmarket_cap)
                csv_writer.writerow(line)

def writedeadcoinsindex(deadcoins,coins,date,links):
    csv_writer=csv.writer(open("allcoins_links.csv",'w',newline=''))
    for i in range(len(deadcoins)):
        line=[]
        line.append(deadcoins[i])
        for j in range(len(coins)):
            if deadcoins[i] in coins[j]:
                appeardate=date[j]
                line.append(appeardate)
                line.append(links[j][coins[j].index(deadcoins[i])])
                break
        
        csv_writer.writerow(line)

if __name__ == "__main__":
    filepath="timedata"
    coins, market_caps, date, links=readcoins(filepath)
    # print(date)
    allcoins = findallcoins(coins)
    # firsttime=writecoinstime(allcoins,coins,market_caps,date)
    writedeadcoinsindex(allcoins,coins,date,links)