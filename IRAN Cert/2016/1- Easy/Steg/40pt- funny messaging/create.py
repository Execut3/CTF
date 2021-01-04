from random import randint

char_set = 'abcdefghijklmnopqrstuvwxyz'
msg = "Hello. Please don't curse me, But sometimes they really send their secrets with this kind of messagings... Flag is APACTF{If_u_think_ab0ut_it_it_w4s_4_little_funny}"

secret = []

for m in msg:
    secret.append(''.join([char_set[randint(0, len(char_set)-1)] for i in range(int(ord(m)))]).strip())

with open('secret.dat', 'w') as outfile:
    outfile.write(','.join(secret))
outfile.close()
    
