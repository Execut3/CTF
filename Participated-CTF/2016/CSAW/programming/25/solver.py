__author__ = 'Execut3'

import socket
from makechange import *
from decimal import Decimal


ip = 'misc.chal.csaw.io'
port = 8000

s = socket.socket()
s.connect((ip,port))


coin_list = [1, 5, 10, 25, 50, 100, 500, 1000, 2000, 5000, 10000, 50000, 100000, 500000, 1000000]

def runAlgorithm(algorithm, message, total_money):
    print algorithm(coin_list, total_money)


def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[change]


def printCoins(coinsUsed,change):
    result = {}
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        if result.has_key(thisCoin):
            result[thisCoin] += 1
        else:
            result[thisCoin] = 1
        coin = coin - thisCoin
    return result


def read_line(s):
    buffer = s.recv(1)
    rec = ''
    while buffer != '\n':
        rec += buffer
        buffer = s.recv(1)
    return rec

count = 0
while True:
    count += 1
    total_money = ''
    print "stage %i" % count
    # line = read_line(s)
    line = s.recv(2048).split('\n')
    print '='
    print line
    for l in line:
        if '$' in l and not 'bill' in l:
            total_money = l.lstrip("$").split(' ')[0]
            print total_money
            continue
    total_money = int(str(int(Decimal(total_money)*100)))
    print total_money
    
    coinsUsed = [0]*(total_money+1)
    coinCount = [0]*(total_money+1)
    dpMakeChange(coin_list,total_money,coinCount,coinsUsed),"coins"
    result = printCoins(coinsUsed,total_money)
    
    # result = changeGreedy2(coin_list, total_money)[0]
    for i in coin_list[::-1]:
        if i == 1 and total_money == 455:
            s.send('1\n')
        if result.has_key(i):
            s.send(str(result[i])+'\n')
        else:
            s.send('0\n')
            
        if not i == 1:
            print s.recv(1024)
        
        # print read_line(s)
        # print s.recv(2048)
    # else:
    #     print s.recv(2048)