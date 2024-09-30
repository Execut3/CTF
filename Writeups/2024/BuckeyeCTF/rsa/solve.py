import Crypto.Util.number as cun
import math

# Given values
e = 65537
n = 66082519841206442253261420880518905643648844231755824847819839195516869801231
c = 19146395818313260878394498164948015155839880044374872805448779372117637653026

# Since p = q, we can find p as the square root of n
def find_prime_when_equal(n):
    p = int(math.sqrt(n))  # Get the integer square root of n
    if p * p == n:  # Check if p squared equals n
        return p, p
    return None, None

# Find p and q (which are the same)
p, q = find_prime_when_equal(n)

# Check if p and q were found
if p and q:
    print(f"p = {p}")
    print(f"q = {q}")

    # Calculate phi(n) for p = q
    phi = p * (p - 1)  # Since phi(n) = p * (p - 1) when p = q

    # Calculate d
    d = pow(e, -1, phi)

    # Decrypt the ciphertext
    m = pow(c, d, n)
    message = m.to_bytes((m.bit_length() + 7) // 8, 'big')

    print(f"Decrypted message: {message.decode()}")
else:
    print("Could not find valid prime p = q such that n = p^2.")
