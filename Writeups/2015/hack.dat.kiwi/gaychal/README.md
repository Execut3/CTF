#Gaychal

**Category: Programming**

```python
import base64
import zlib

chalFile = open('gaychal.txt','r').readlines()[0]

decoded = chalFile
while decoded.find('eval')>-1:
    print decoded[:50]
    if decoded.find('eval(base64_decode')>-1:
        data = decoded.split('\'')[1]
        decoded = base64.b64decode(data)
    elif decoded.find('pack')>-1:
        data = decoded.split('\'')[3]
        decoded = data.decode('hex')
    elif decoded.find('gzuncompress')>-1:
        print 'in gzuncompress'
        data = decoded.split('\'')[1]
        data = base64.b64decode(data)
        decoded = zlib.decompress(data)
    elif decoded.find('hex2bin')>-1:
        data = decoded.split('\'')[1]
        decoded = data.decode('hex')
        print 'after hex2bin: ' + decoded[:50]
    else:
        print 'not handled'

print decoded
```

Decoding will result this:

```
echo "the flag is ".md5("5+5=9<-- fix this"),PHP_EOL;
```

