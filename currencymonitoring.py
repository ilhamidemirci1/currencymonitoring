from bs4 import BeautifulSoup
import requests
import pywhatkit as kit
import time

while True:
    ## USD
    urlusd = "https://www.google.com/finance/quote/USD-TRY?hl=tr"  
    sayfa = requests.get(urlusd)
    html_sayfa = BeautifulSoup(sayfa.content, "html.parser")
    dolar = html_sayfa.find("div", class_="YMlKec fxKbKc").getText() 
    roundeddolar = round(float(dolar.replace(",", ".")), 2)
    USDmsg = "1USD = " + str(roundeddolar) + "TL"

    ## EUR
    urlEUR = "https://www.google.com/finance/quote/EUR-TRY?hl=tr"
    sayfa2 = requests.get(urlEUR)
    html_sayfa2 = BeautifulSoup(sayfa2.content, "html.parser")
    eur = html_sayfa2.find("div", class_="YMlKec fxKbKc").getText()
    roundedEUR = round(float(eur.replace(",", ".")), 2)
    EURmsg = "1EUR = " + str(roundedEUR) + "TL"

    ## ÇeyrekAltınAlış
    urlau = "https://bigpara.hurriyet.com.tr/altin/ceyrek-altin-fiyati/#:~:text=%C3%87eyrek%20Alt%C4%B1n%20fiyat%C4%B1%20ne%20kadar,sat%C4%B1%C5%9F%20fiyat%C4%B1%202800%20TL%20%C5%9Feklindedir."
    sayfa3 = requests.get(urlau)
    html_sayfa3 = BeautifulSoup(sayfa3.content, "html.parser")
    au1 = html_sayfa3.find("span", class_="value up").getText()
    AUmsg = "Ceyrek Alis = " + str(au1) + "TL"

    kit.sendwhatmsg ("#enter phone number +905..", USDmsg + "\n" + EURmsg + "\n" + AUmsg, time.localtime().tm_hour, time.localtime().tm_min + 1)

    time.sleep(3600)  # Wait for 1 hours before fetching and sending again
