from bs4 import BeautifulSoup
import requests

url="https://coinmarketcap.com/historical/"
head={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
r=requests.get(url,head)

while(r.status_code!=200):
    r=requests.get(url,head)
soup=BeautifulSoup(r.text,"html.parser")

page=soup.find("div",{"class":"col-xl-10 padding-top-1x"})
year=page.findAll("div",{"class":"row"})
# results2=soup.findAll("h2",{"class":"text-center margin-bottom--lv4"})
# results2=soup.findAll("a",{"class":"currency-name-container"})

f=open("catalogue.csv","w")
# f.write("time,pagelink\n")

print(len(year))
for i in range(len(year)):
    print(year[i].h2.string)
    month = year[i].findAll("div",{"class":"col-sm-4 col-xs-6"})
    for j in range(len(month)):
        print(month[j].h3.string)
        # week = month[j].ul.li.a.string
        week = month[j].findAll("li",{"class":"text-center"})
        for m in range((len(week))):
            print(week[m].a.string)
            # print(week[m].a.attrs["href"])
            href= "https://coinmarketcap.com/"+week[m].a.attrs["href"]
            f.write(year[i].h2.string+" "+month[j].h3.string+" "+week[m].a.string+","+href)
            f.write("\n")
f.close()