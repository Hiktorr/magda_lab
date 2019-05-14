import requests
from random import random, randint
from time import sleep
#functions

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

#classes

class userWallet:
    btc = []
    usd = []

    def __init__(self, btc = None, usd = None):
        if btc is None:
            btc = random()
        if usd is None:
            usd = random()*1000
        self.btc = btc
        self.usd = usd

    def addToWallet(self, currency, amount):
        if currency.lower() == 'usd':
            self.usd += amount
        if currency.lower() == 'btc':
            self.btc += amount

    def removeFromWallet(self, currency, amount):
        if currency.lower() == 'usd':
            self.usd -= amount
        if currency.lower() == 'btc':
            self.btc -= amount

    def getWallet(self):
        return self.btc, self.usd


class randomUser:
    id = None
    username = []
    wallet = []

    def __init__(self, id, btc= None, usd= None):
        self.username = self.getUsernameFromServer()
        self.wallet = userWallet(btc, usd)
        self.id = id

    def getUsernameFromServer(self):
        users = requests.get("https://randomuser.me/api/")
        dataUsers = users.json()
        firstName = dataUsers['results'][0]['name']['first']
        lastName = dataUsers['results'][0]['name']['last']
        return firstName, lastName

    def getUsername(self):
        return self.username

    def getUserWallet(self):
        return self.wallet.getWallet()

    def addToUserWallet(self, currency, amount):
        self.wallet.addToWallet(currency, amount)

    def removeFromUserWallet(self, currency, amount):
        self.wallet.removeFromWallet(currency, amount)

class marketSimulator:
    users = []
    bitBayMarket = []

    def __init__(self, loops=None):
        if loops is None:
            loops = 100
        for i in range(loops):
            self.users.append(randomUser(i))
        self.bitBayMarket = getFromBitBay()
        print("Users created!")

    def printUsers(self):
        for user in self.users:
            print("Username: {} {} | Wallet: {} BTC, {} USD".format(user.getUsername()[0].capitalize(), user.getUsername()[1].capitalize(), user.getUserWallet()[0], user.getUserWallet()[1]))

    def makeTransaction(self):
        firstUserIndex = randint(0,len(self.users)-1)
        secondUserIndex = randint(0,len(self.users)-1)
        while firstUserIndex is secondUserIndex:
            secondUserIndex = randint(0,len(self.users)-1)
        sellAmount = random()/10
        #sell btc
        if sellAmount < self.users[firstUserIndex].getUserWallet()[0] and sellAmount*self.bitBayMarket[1] < self.users[secondUserIndex].getUserWallet()[1]:
            self.users[firstUserIndex].removeFromUserWallet('btc',sellAmount)
            self.users[firstUserIndex].addToUserWallet('usd',sellAmount*self.bitBayMarket[0])
            self.users[secondUserIndex].removeFromUserWallet('usd',sellAmount*self.bitBayMarket[1])
            self.users[secondUserIndex].addToUserWallet('btc',sellAmount)
            print("{} {} exchanged {} BTC with {} {} for {} USD.".format(self.users[firstUserIndex].getUsername()[0].capitalize(), self.users[firstUserIndex].getUsername()[1].capitalize(), sellAmount, self.users[secondUserIndex].getUsername()[0].capitalize(), self.users[secondUserIndex].getUsername()[1].capitalize(), sellAmount*self.bitBayMarket[1]))
            return True
        else:
            print("Transaction canceled. Not sufficient funding")
            return False

    def simulateMultipleTransactions(self, numberOfTransactions = None, waitTime = None):
        if numberOfTransactions is None:
            numberOfTransactions = 1000
        if waitTime is None:
            waitTime = 5
        confirmedTransaction = 0
        unconfirmedTransaction = 0

        while confirmedTransaction+unconfirmedTransaction <= 1000:
            if self.makeTransaction():
                confirmedTransaction += 1
            else:
                unconfirmedTransaction +=1
            print("CONFIRMED: {}   |   UNCONFIRMED: {}".format(confirmedTransaction, unconfirmedTransaction))
            sleep(waitTime)

#main

x = marketSimulator(20)

x.printUsers()
x.simulateMultipleTransactions(1000,0)
x.printUsers()