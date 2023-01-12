from __future__ import absolute_import

import base64
import socket
import string
import hashlib
try:  # pragma: no cover
  import psyco
  psyco.full()
except ImportError:  # pragma: no cover
  psyco = None
# pylint: enable-msg=R0801

from mom import _compat
from mom import builtins
from mom import string
from mom.codec import _base

Morse = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }

def to_morse(text):
    result = []
    for t in text:
        for key,value in Morse.items():
            if t == key:
                result.append(value)
                break
    return ' '.join(result)

EMPTY_BYTE = _compat.EMPTY_BYTE

# Follows ASCII order.
ASCII36_BYTES = (string.DIGITS +
                 string.ASCII_UPPERCASE).encode("ascii")
# Therefore, b"1" represents b"\0".
if _compat.HAVE_PYTHON3:
  ASCII36_BYTES = tuple(builtins.byte(x) for x in ASCII36_BYTES)


def b36encode(raw_bytes, base_bytes=ASCII36_BYTES, _padding=True):
  """
  Base-36 encodes a sequence of raw bytes. Zero-byte sequences are
  preserved by default.

  :param raw_bytes:
      Raw bytes to encode.
  :param base_bytes:
      The character set to use. Defaults to ``ASCII36_BYTES``
      that uses natural ASCII order.
  :param _padding:
      (Internal) ``True`` (default) to include prefixed zero-byte sequence
      padding converted to appropriate representation.
  :returns:
      Uppercase (default) base-36 encoded bytes.
  """
  return _base.base_encode(raw_bytes, 36, base_bytes, base_bytes[0], _padding)


def b36decode(encoded, base_bytes=ASCII36_BYTES):
  """
  Base-36 decodes a sequence of bytes into raw bytes.

  Leading, trailing, and internal whitespace is ignored. The case
  of the encoded byte string is also ignored. For example, you may pass
  in ``AbCd`` instead of ``ABCD``.

  :param encoded:
      Case-insensitive base-36 encoded bytes.
  :param base_bytes:
      (Internal) The character set to use. Defaults to ``ASCII36_BYTES``
      that uses natural ASCII order.
  :returns:
      Raw bytes.
  """
  # Ignore whitespace.
  encoded = EMPTY_BYTE.join(encoded.split())
  return _base.uint_to_base256(int(encoded, 36), encoded, base_bytes[0])

address = 'morset.pwning.xxx'
port = 11821
s = socket.socket()
s.connect((address,port))  


print '[+] Starting'
text = s.recv(1024).strip()
tmp_text = ''
for i in text:
    if i != ' ':
        tmp_text += '-' if i == '.' else '.'
    else:
        tmp_text += ' '
text = text.split(' ')
result = ''
for t in text:
    for key,value in Morse.items():
        if value == t:
            result += key
            break
b36d = b36decode(result).split('\n')
sh = b36d[-1].split('(')[1].split(')')[0]
sh256 = hashlib.sha256(sh).hexdigest()
morse_back = to_morse(b36encode(sh256))
print '[+] Sending'
s.send(morse_back+'\n')
text = s.recv(1024)

text += s.recv(1024)
text = text.strip().split(' ')
result = ''
for t in text:
    for key,value in Morse.items():
        if value == t:
            result += key
            break
print b36decode(result)