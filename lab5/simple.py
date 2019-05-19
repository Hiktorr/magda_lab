import requests
from random import random, randint
from time import sleep

def getFromBitBay():
    bitBay = requests.get("https://bitbay.net/API/Public/BTC/ticker.json")
    dataBitBay = bitBay.json()
    bestBid_BB=dataBitBay['bid']
    bestAsk_BB=dataBitBay['ask']
    return bestBid_BB, bestAsk_BB

listOfUsers = []
listOfWallets = []


numberOfUsers = 4
transactionPerMinute = 60
allTransactionAmount = 1000

for i in range(numberOfUsers):
    users = requests.get("https://randomuser.me/api/")
    dataUsers = users.json()
    firstName = dataUsers['results'][0]['name']['first']
    lastName = dataUsers['results'][0]['name']['last']
    listOfUsers.append([i+1, firstName, lastName])
    listOfWallets.append([random()*10000, random()])


sellAmount = random()/10

BTCUSD, USDBTC = getFromBitBay()

currentTransactionAmount = 0
while(currentTransactionAmount != allTransactionAmount):
    firstUserIndex = randint(0, numberOfUsers - 1)
    secondUserIndex = randint(0, numberOfUsers - 1)
    while firstUserIndex == secondUserIndex:
        secondUserIndex = randint(0, numberOfUsers - 1)
    sellAmount = random() / 10
    if sellAmount < listOfWallets[firstUserIndex][1] and sellAmount*USDBTC < listOfWallets[secondUserIndex][0]:
        print("{} {} exchanged {} BTC with {} {} for {} USD.".format(listOfUsers[firstUserIndex][1],listOfUsers[firstUserIndex][2],sellAmount,listOfUsers[secondUserIndex][1],listOfUsers[secondUserIndex][2], sellAmount* USDBTC))
        listOfWallets[firstUserIndex][1] -= sellAmount
        listOfWallets[secondUserIndex][1] += sellAmount
        listOfWallets[firstUserIndex][0] += sellAmount*BTCUSD
        listOfWallets[secondUserIndex][0] += sellAmount*USDBTC
    else:
        print("Transaction canceled. Not sufficient funding")
    sleep(60 / transactionPerMinute)
    currentTransactionAmount += 1

