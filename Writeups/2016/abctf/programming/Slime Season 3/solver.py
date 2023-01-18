# Quarter 25c
# Dime 10c
# Penny 1c

def sumtototal(total, coins_list):
    s = [0]
    for i in range(1, total+1):
        s.append(-1)
        for coin_val in coins_list:
            if i-coin_val >=0 and s[i-coin_val] != -1 and (s[i] > s[i-coin_val] or s[i] == -1):
                s[i] = 1 + s[i-coin_val]

    print s
    return s[total]

total = input()
coins_list = map(int, raw_input().split(' '))
print sumtototal(total, coins_list)