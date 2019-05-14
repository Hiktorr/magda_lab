import requests

def getFromTiingo():
    tiingo = requests.get("https://api.tiingo.com/tiingo/crypto/top?tickers=btcusd&token=5ae14e499938caf8d9f51ad398e80df834a5cd6a")
    dataTiingo = tiingo.json()
    bestBid_Ti=(dataTiingo[0]['topOfBookData'][0]['bidPrice'])
    bestAsk_Ti=(dataTiingo[0]['topOfBookData'][0]['askPrice'])
    return bestBid_Ti, bestAsk_Ti

def getFromBitBay():
    bitBay = requests.get("https://bitbay.net/API/Public/BTC/ticker.json")
    dataBitBay = bitBay.json()
    bestBid_BB=dataBitBay['bid']
    bestAsk_BB=dataBitBay['ask']
    return bestBid_BB, bestAsk_BB

Tiingo = getFromTiingo()
BitBay = getFromBitBay()
print(Tiingo, BitBay)
if Tiingo[0] > BitBay[0] and Tiingo[1] > BitBay[1]:
    print("Currently the BitBay exchange market is better for buying whilst Tiingo is better for selling")
elif Tiingo[0] < BitBay[0] and Tiingo[1] > BitBay[1]:
    print("Currently the BitBay exchange market is better for buying whilst BitBay is better for selling")
elif Tiingo[0] > BitBay[0] and Tiingo[1] < BitBay[1]:
    print("Currently the Tiingo exchange market is better for buying whilst Tiingo is better for selling")
elif Tiingo[0] < BitBay[0] and Tiingo[1] < BitBay[1]:
    print("Currently the Tiingo exchange market is better for buying whilst BitBay is better for selling")