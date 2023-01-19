#Bsniff

**Category:** Forensics

To find the flag, reconstruct what the user was actually looking for.

##Solution

This challenge is more steganography & sort of a covert challenge!
In this task we are given a .pcap file which is a captured file of a network traffic that is trying to send flag throught
an hidden channel whithin url requests to blockchain.info website.

Looking at .pcap file using wireshark, i noticed that there are strange requests to "blockchain.info/q/addressbalance/".
Looks like some Base64 encoded like data had been transfered throught this requests. "Follow tcp stream" on each of these request streams will give us something like below:

```
GET /q/addressbalance/1KBtNgrukDEDiWjrqirzqeiSTL77zLFrVL?confirmations=6 HTTP/1.1
Host: blockchain.info
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: python-requests/2.4.3 CPython/2.7.9 Linux/3.16.0-4-amd64
```

At first we thought that these data is base64 encoded and a file or something is transfered by this characters. so i tried to put them together to get some file as result, but impossible.
After wasting a lot of time on finding out how to solve this challenge, By the help of my teammates we noticed that
some characters are not send throught this urls and There are 41 '?' signs in requests which mean 41 characters are missing.

```
1FbACt9mRncgM2JAButUJerYhpQkN9?bcV
1AKe3rg4SzdSzR9?nG3wddKkbnstFW3JzU
18MDLgXS1mnoiNQ6p17B18Se9z4JDhrz?5
1AegmEokZKRCWeMW4vrsgqCvL?1Wf5RNv
17eNk?Xo1Kc7KL59H1ndqkXE8USob2dghC
15DdBDZ8M32UHDzdbMyJBLLkmowZ?Migt4
1CSRjBzRJcFHxS4db8nLiv?Qv4zkBTsxP2
1MWn8sPA9UpksgQ73LZeR?35R44DsiUM9v
17GJvFgdUsiitxGpMhFphas?Lk3RkZCeQX
1JUggm1WKhJvZa1JB?vgr3v5Mf2vnqknT3
1D9?ZQftnkN3PcDuPPmE5ML3744puyjgsS
18zZiP4UubYh9wjGWmq?nMV7ntnUb3MWGu
19?7JpEcHrrkwTTKtXz8ZRAHoKH8vqmxKg
1GaUtT9Pd6VC6B?Hudophj2jWf6noc7aFp
19MTQ1ujn?zCB6B4ML6YFszpHzwwmHVmEP
19MTQ?ujn7zCB6B4ML6YFszpHzwwmHVmEP
12ED?tLKFZWZsWCgYEJv6vQMAX1jerhkxD
1GBZ?hceFBsexguZEJz4k4cTWSEfKq1fkx
1JUggm?WKhJvZa1JB1vgr3v5Mf2vnqknT3
1?jzRjqsuhSSA123ABGpX7Tv1QE6vvwJiw
1C1?HgHSMu3fURquTaEDaD5BvgTwmD17WU
13eN1f?ebMdL6HxTxVyLcuJEtay34meobY
16SgUK8nprEuXKD7JgyuPnrhKqN?JynpY9
1A71jVtkA?o5D2tDDQvyua6YqDJT7nmWQp
1FtuVHgzU8oCkfVRaseApKkb?qSs6hqvDv
1Fba7UPrx8hy7n8VS3qJgS3KL4kkPSd?fr
15s6yYhzVsrM?9nBi1geaJuBZFGQtMdhA6
1jyyFnru16GVAEK9jZfH4Rx2kj?fxvc7Z
1?wF9bkpiG6YULrDsC5Z7C1kG3vcR4pP5
1KPof64jhmzoDrd18c?g9PmeNv6zPDJ7GM
1NXKUBntDYDJMNYoMQcB?FnJQmh66Efw9p
155ZkHWajMr8Ueou?8CHT1GRrhEAPdUScZ
19caJfenSseY5LVVbN66dGnV4PZwP?ACKV
1NWnafub?gAc9FB82o7QXmLEYB2wzEsMWL
17GJvFg?UsiitxGpMhFphas3Lk3RkZCeQX
126AvtA56BS?SshcdidNqMN9gH2B7AxZLi
1LBcGjboLF?nb2xAvxqRxnKfMVuq9jdM8W
1JWiY3y46VvJT?Rbg6hzaRDdrcHUxvj2PN
1D?1XsL3scgZqCGJfB7Hx5vYNy7Qf9becd
1GW83NnA?ZSkMw3XcNA5kSvw55RRcjgWGv
1HTKZdD?PCAmjQY18CTDTVFE1rcQpCpDAQ
```

Now the problem was how to find these values.
But again we noticed that if we send that request again to "blockchain.info/q/addressbalance/", we might get usefull data.
Cause when the request is not correct we will get responses like "checksum not valid", but if the request is correct it returns an integer value instead.
So again the task was clear, we should brute these requests to get the right value. Doing this will give us this character sequence:

```
be6ai1ed31a1fb718r18efeFe627Sb2ec5d39dhTC
```

Looking at this string, we will notice that we have all needed characters for SharifCTF which represent the flag. But the position of characters is wrong.
So i save the position of occurence of each character in each url request of .pcap file. (Again thanks to my teammate for finding out this tricky tip)

```python
{1: '8S', 2: 'fh', 3: 'ae', 4: '8r', 5: 'i1', 6: '1f', 7: 'dC', 8: '5T', 9: '7F', 10: '9', 11: '3', 12: '2', 13: 'd', 14: 'b', 15: 'e', 16: 'e', 17: '1', 18: 'b', 19: '1', 20: '2', 21: 'd', 22: 'e', 23: '3', 24: 'e', 25: 'a', 26: '7', 27: 'e', 28: '1', 29: 'c', 30: 'b', 31: '6', 32: '6'}
```

Now we just have to reorder this values by their position number which will give us the flag.

Python code to solve this challenge (the dirty one :D)

```python
import pyshark
import urllib
import requests
import itertools
import re
import json

chars = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/'

result = {}
outfile = open('all_info.out', 'w')
pkts = pyshark.FileCapture('bsniff.pcap')
count = 0
for pkt in pkts:
    try:
        content = str(pkt.http).split('\n')
    except:
        continue
    for c in content:
        if 'GET /q/addressbalance' in c:
            r = c.split('GET /q/addressbalance/')[1].split('?confirmations=6')[0]
            break
    if r:
        count += 1
        if '?' in r:
            ch = '-'
            req_text = ''
            for xs in itertools.product(chars, repeat=1):
                n_r = r.replace('?', ''.join(xs))
                url = 'https://blockchain.info/q/addressbalance/{0}?confirmations=6'.format(n_r)
                req = requests.get(url)
                try:
                    int(req.text)
                    break
                except:
                    continue
            print '{0},{1}'.format(r.index('?'), ''.join(xs))
            result[r.index('?')] = ''.join(xs)
print result
```