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

def main():
    amnt = 63
    clist = [1, 5, 10, 25, 50, 100, 500, 1000, 2000, 5000, 10000, 50000, 100000, 500000, 1000000]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)
    

    print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
    print printCoins(coinsUsed,amnt)
    print(coinsUsed)

main()
