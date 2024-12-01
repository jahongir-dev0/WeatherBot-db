import requests
from aiogram.types import Message

from bs4 import BeautifulSoup as BS

def harorat(viloyat):
    link = f"https://obhavo.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce,'html.parser')
    max = soup.select('.forecast-day')[0].text
    print(max)
    return max

def min(viloyat):
    link = f"https://obhavo.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce,'html.parser')
    min= soup.select('.forecast-night')[0].text
    return min

def tong(viloyat):
    link = f"https://obhavo.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce,'html.parser')
    tong = soup.select('.forecast')[0].text
    return tong
def kunh(viloyat):
    link = f"https://obhavo.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce,'html.parser')
    kun = soup.select('.col-2 .forecast')[0].text
    return kun

def oqshom(viloyat):
    link = f"https://obhavo.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce,'html.parser')
    oqshom = soup.select('.col-3 .forecast')[0].text
    return oqshom
def kun(viloyat):
    link = f"https://obhavo.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce, 'html.parser')
    kun = soup.select(".current-day")[0].text
    return kun

def Viloyat(viloyatt):
    link = f"https://obhavo.uz/{viloyatt}"
    responce = requests.get(link).text
    soup = BS(responce, 'html.parser')
    viloyat = soup.find("h2").text
    return viloyat

def obhavo(viloyat):
    link = f"https://obhavo.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce, 'html.parser')
    obhavo= soup.select(".current-forecast-desc")[0].text
    return obhavo

def Oy(viloyat):
    link = f"https://obhavo.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce, 'html.parser')
    obhavo= soup.select(".col-2")[0].text
    return obhavo

def Namlik(viloyat):
    link = f"https://obhavo.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce, 'html.parser')
    namlik= soup.select(".col-1")[0].text
    return namlik

#_______________________RUS____________________________
def haroratru(viloyat):
    link = f"https://pogoda.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce,'html.parser')
    max = soup.select('.forecast-day')[0].text
    print(max)
    return max

def minru(viloyat):
    link = f"https://pogoda.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce,'html.parser')
    min= soup.select('.forecast-night')[0].text
    return min

def tongru(viloyat):
    link = f"https://pogoda.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce,'html.parser')
    tong = soup.select('.forecast')[0].text
    return tong
def kunhru(viloyat):
    link = f"https://pogoda.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce,'html.parser')
    kun = soup.select('.col-2 .forecast')[0].text
    return kun

def oqshomru(viloyat):
    link = f"https://pogoda.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce,'html.parser')
    oqshom = soup.select('.col-3 .forecast')[0].text
    return oqshom
def kunru(viloyat):
    link = f"https://pogoda.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce, 'html.parser')
    kun = soup.select(".current-day")[0].text
    return kun

def Viloyatru(viloyatt):
    link = f"https://pogoda.uz/{viloyatt}"
    responce = requests.get(link).text
    soup = BS(responce, 'html.parser')
    viloyat = soup.find("h2").text
    return viloyat

def obhavoru(viloyat):
    link = f"https://pogoda.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce, 'html.parser')
    obhavo= soup.select(".current-forecast-desc")[0].text
    return obhavo

def Oyru(viloyat):
    link = f"https://pogoda.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce, 'html.parser')
    obhavo= soup.select(".col-2")[0].text
    return obhavo

def Namlikru(viloyat):
    link = f"https://pogoda.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce, 'html.parser')
    namlik= soup.select(".col-1")[0].text
    return namlik


