#!/usr/bin/env python
import sys

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Execption happened.')
    else:
        return x % m


flag = 'Nice job, flag is APACTF{N!C3_J08_D3CRYP7!NG_M3}'
base = 10
p = 12131072439211271897323671531612440428472427633701410925634549312301964373042085619324197365322416866541017057361365214171711713797974299334871062829803541
q = 12027524255478748885956220793734512128733387803682075433653899983955179850988797899869146900809131611153346817050832096022160146366346391812470987105415233
e = 65537

n = p * q
phi = (p - 1) * (q - 1)
d = modinv(e, phi)

# Encrypting secret
m = flag.encode('hex')
m = int('0x' + m, 16)
encrypted = pow(m, e, n)
print encrypted
open('data.secret', 'w').write(hex(encrypted)[2:-1].decode('hex'))


# Decrypting secret
c = int('0x' + open('data.secret', 'r').read().strip().encode('hex'), 16)
x = pow(c, d, n)
decrypted = hex(x)[2:-1].decode('hex')
print decrypted
