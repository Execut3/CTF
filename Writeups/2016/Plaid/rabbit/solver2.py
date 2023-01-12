from Crypto.Util.number import getPrime, getRandomRange, GCD

def getBlumPrime(nbits):
    p = getPrime(nbits)
    while p % 4 != 3:
        p = getPrime(nbits)
    return p

def genKey(nbits):
    p = getBlumPrime(nbits/2)
    q = getBlumPrime(nbits/2)
    N = p * q
    return ((p,q), N)

def randQR(N):
    return pow(getRandomRange(1, N), 2, N)

def encrypt(m, N):
    return pow(m, 2, N)

def legendreSymbol(a, p):
    return pow(a, (p-1)/2, p)

def decrypt(c, p, q):
    if GCD(c, p*q) != 1:
        return False
    if legendreSymbol(c, p) != 1:
        return False
    if legendreSymbol(c, q) != 1:
        return False
    return pow(c, ((p-1)*(q-1) + 4) / 8, p*q)

N_tmp = 81546073902331759271984999004451939555402085006705656828495536906802924215055062358675944026785619015267809774867163668490714884157533291262435378747443005227619394842923633601610550982321457446416213545088054898767148483676379966942027388615616321652290989027944696127478611206798587697949222663092494873481
flag_tmp = 16155172062598073107968676378352115117161436172814227581212799030353856989153650114500204987192715640325805773228721292633844470727274927681444727510153616642152298025005171599963912929571282929138074246451372957668797897908285264033088572552509959195673435645475880129067211859038705979011490574216118690919

flag = '15'
flag = long(flag)
pq, N = genKey(7)
print pq
p = pq[0]
q = pq[1]
for i in range(71,72):
    
    t = decrypt(i, p,q)
    if t != False:
        print i
        print t

# for i in range(2,3):
#     if i % 100 == 0:
#         print i
#     pq, N = genKey(i)
#         
#     print N
#     if N == N_tmp:
#         
#         print i
#         break
    