We are given the source code below, which is an implementation of RSA alg.
```python
import Crypto.Util.number as cun
import math

message = b"bctf{fake_flag}"

m = int.from_bytes(message, "big")

p = cun.getPrime(128)
q = cun.getPrime(128)
e = 65537

n = p * q
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
assert (e * d) % phi == 1
assert math.gcd(e, phi) == 1

c = pow(m, e, n)

print(f"e = {e}")
print(f"n = {n}")
print(f"c = {c}")

"""
Output:
e = 65537
n = 66082519841206442253261420880518905643648844231755824847819839195516869801231
c = 19146395818313260878394498164948015155839880044374872805448779372117637653026
"""
```

We have e, n ,c parameters. I used RsaCtfTool to decrypt the cipher.

```bash
python RsaCtfTool.py -n 66082519841206442253261420880518905643648844231755824847819839195516869801231 -e 65537 --decrypt 19146395818313260878394498164948015155839880044374872805448779372117637653026
private argument is not set, the private key will not be displayed, even if recovered.
['/tmp/tmpbss_ib25']

[*] Testing key /tmp/tmpbss_ib25.
attack initialized...
attack initialized...
[*] Performing lucas_gcd attack on /tmp/tmpbss_ib25.
100%|██████████████████████████████████████████████████████████████████████| 9999/9999 [00:00<00:00, 331320.23it/s]
[+] Time elapsed: 0.0342 sec.
[*] Performing rapid7primes attack on /tmp/tmpbss_ib25.
[+] loading prime list file data/ea229f977fb51000.pkl.bz2...
loading pickle data/ea229f977fb51000.pkl.bz2...
100%|███████████████████████████████████████████████████████████████████| 61174/61174 [00:00<00:00, 2298218.92it/s]
[+] loading prime list file data/fbcc4333b5f183fc.pkl.bz2...
loading pickle data/fbcc4333b5f183fc.pkl.bz2...
100%|███████████████████████████████████████████████████████████████████| 21048/21048 [00:00<00:00, 2139125.53it/s]
[+] Time elapsed: 0.2889 sec.
[*] Performing smallq attack on /tmp/tmpbss_ib25.
[+] Time elapsed: 0.1870 sec.
[*] Performing mersenne_primes attack on /tmp/tmpbss_ib25.
 24%|█████████████████▍                                                        | 12/51 [00:00<00:00, 390167.81it/s]
[+] Time elapsed: 0.0005 sec.
[*] Performing pastctfprimes attack on /tmp/tmpbss_ib25.
[+] loading prime list file data/visa_emv.txt...
100%|█████████████████████████████████████████████████████████████████████████████| 2/2 [00:00<00:00, 45343.83it/s]
[+] loading prime list file data/ti_rsa_signing_keys.txt...
100%|█████████████████████████████████████████████████████████████████████████| 34/34 [00:00<00:00, 1064226.39it/s]
[+] loading prime list file data/pastctfprimes.txt...
100%|███████████████████████████████████████████████████████████████████████| 121/121 [00:00<00:00, 1600980.39it/s]
[+] Time elapsed: 0.0017 sec.
[*] Performing fibonacci_gcd attack on /tmp/tmpbss_ib25.
100%|██████████████████████████████████████████████████████████████████████| 9999/9999 [00:00<00:00, 297080.44it/s]
[+] Time elapsed: 0.0341 sec.
[*] Performing factordb attack on /tmp/tmpbss_ib25.
[*] Attack success with factordb method !
[+] Total time elapsed min,max,avg: 0.0005/0.2889/0.0911 sec.

Results for /tmp/tmpbss_ib25:

Decrypted data :
HEX : 0x00626374667b663463373072317a335f6233373733725f34643362333565347d
INT (big endian) : 173837423383044571441359179355396996357282245146783171632617116789291431037
INT (little endian) : 56631680630946298057315686547894562665178625861157125497183263120345694167552
utf-8 : bctf{flaghere}
utf-16 : 戀瑣筦㑦㝣爰稱弳㍢㜷爳㑟㍤㍢攵紴
STR : b'\x00bctf{flaghere}'

```