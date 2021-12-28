from songline import Sendline

import requests
import time

from pprint import pprint

from binance.client import Client
api_key = "----"
api_secret ="----"
token = "----"
messenger = Sendline(token)

total_result = ""



API_HOST = 'https://api.bitkub.com'
main_coinkub = ["THB_USDT"]
coinkub = ["THB_KUB","THB_SIX","THB_JFIN"]
coinbnb = ["SLPUSDT"]
while True:
    total_result = ""
    client = Client(api_key, api_secret)
    prices = client.get_all_tickers()
    response = requests.get(API_HOST + "/api/market/ticker")
    result = response.json()
    for m in main_coinkub:
        sym = m
        data = result[sym]
        last = data["last"]
        THB = float(last)
        #print(THB)
    for d in coinkub:
        sym2 = d
        data = result[sym2]
        last = data["last"]
        THB = float(last)
        #print(sym2, last)
        #messenger.sendtext(sym2 + " : " + str(last))
        total_result += sym2 + " " + str(last) + '                       '
    #messenger.sendtext("Live Price" + "\n" +total_result)     
    for p in prices:
        for c in coinbnb:
            sym3 = c
            if p["symbol"] == sym3:
                TOTHB = float(p["price"])
                rate = (TOTHB * THB)/2
                print(sym3, rate)
                messenger.sendtext("Live Price" + "\n" +total_result + "{} : {:,.3f} -----------------------------".format(sym3,rate))
    if rate >= 10:
        messenger.sendtext("SLP ขึ้น 10 แล้ว!!!!!!!!! ")
                
    print("---")
    time.sleep(1)




    
