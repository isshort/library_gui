import requests
from bs4 import BeautifulSoup

url="http://acmp.ru/index.asp?main=rating&str=+%E4%EE%F2%E0+2"

response=requests.get(url)

html_icerigi=response.content

soup=BeautifulSoup(html_icerigi,"html.parser")
liste=[]
for i in soup.find_all("tr",{"class":"white"}):
    bilgi=i.text
    bilgi=bilgi[:-1]
    liste.append(bilgi)
    with open("file.txt","w")as file:
        for i in liste:
            file.write(i)
liste1=[]
with open("file.txt",'r')as file12:
    ekle=file12.readlines()
    for bilgi in ekle:
        bilgi=bilgi[:-1]
        bilgi=bilgi.lstrip()
        liste1.append(bilgi)
   
sizeofarray=len(liste1)
print(sizeofarray)
n = sizeofarray//5+1
m = 5
h=1
a = [[0] * m] * n
for row in range(len(a)-1):
    for column in range(len(a[row])):
        a[row][column]=liste1[h]
        h+=1
        print(a[row][column],end=" ")
    print()
