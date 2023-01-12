# openssl rsa -in out.pub -pubin -text -modulu


# $ openssl rsa -in out.pub -pubin -text -modulus
# Public-Key: (256 bit)
# Modulus:
#     00:a6:35:06:e1:5c:68:e3:ee:24:7d:a2:5c:84:a9:
#     0f:66:f9:e9:b6:66:d1:9f:a5:2e:66:61:a3:70:51:
#     6f:7a:eb
# Exponent: 65537 (0x10001)
# Modulus=A63506E15C68E3EE247DA25C84A90F66F9E9B666D19FA52E6661A370516F7AEB
# writing RSA key
# -----BEGIN PUBLIC KEY-----
# MDwwDQYJKoZIhvcNAQEBBQADKwAwKAIhAKY1BuFcaOPuJH2iXISpD2b56bZm0Z+l
# LmZho3BRb3rrAgMBAAE=
# -----END PUBLIC KEY-----


# Now fire up 'yafu' to find p and q, cause of rsa.pub week
# factor(0xA63506E15C68E3EE247DA25C84A90F66F9E9B666D19FA52E6661A370516F7AEB)

# ***factors found***
# 
# P39 = 269077763884745563624960620392345050013    ---> p
# P39 = 279389950920115298845886167682594209319    ---> q
# 
# ans = 1


# Updating solver.py and run python solver.py
# python solver.py 
# APACTF{T0o0_w3e3e3k}


from Crypto.Util.number import *
import base64

def egcd(a, b):
    u, u1 = 1, 0
    v, v1 = 0, 1
    while b:
        q = a // b
        u, u1 = u1, u - q * u1
        v, v1 = v1, v - q * v1
        a, b = b, a - q * b
    return a, u, v

def decrypt(p, q, e, n, ct):
    phi = (p - 1) * (q - 1)
    gcd, a, b = egcd(e, phi)
    d = a
    if d < 0:
        d += phi
    pt = pow(ct, d, n)
    print(long_to_bytes(pt))

m1 = base64.b64decode('PNU6VRL6dCGLVO9yegiLsH38mwoO+CALdyJzMMayCzM=')


p = 269077763884745563624960620392345050013
q = 279389950920115298845886167682594209319
e = 65537
n = 0xA63506E15C68E3EE247DA25C84A90F66F9E9B666D19FA52E6661A370516F7AEB
decrypt(p, q, e, n, bytes_to_long(m1))
