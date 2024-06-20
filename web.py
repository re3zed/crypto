from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import URLError
from time import sleep
f=True
#while f:
try:
    lis={}
    f=0.0
    b=input(int("num:"))
    html=urlopen("https://coinranking.com")
    bs=BeautifulSoup(html.read(),"lxml")
    find=bs.find_all("div",{"class":"valuta"})
    for i in range(0,b,2):
      #print(find[i])
      #print(find[i].get_text())
      price=find[i].get_text().replace('$', '').replace(' ', '').replace('\n','').replace(',','')
      price_string=float(price)
      #pricee=float(price_string)
      f+=price
      g=b/2
      z=f/g
      print(z)



      #print(i,'-',float(price_string))
        

except URLError as u:
  print("nt")
  f=True
  sleep(1)
else:
   f=False