#!/usr/local/bin/python3.2
# coding: utf-8

import os
import re
import sys
import cgi

from urllib import parse
import binascii

import urllib
import urllib.request

print('Content-Type: text/html\n\n')

request = cgi.FieldStorage() 
url  = request.getvalue('url') or ''

if url:
    if len(url) > 50:
        print('Sorry but maximum allowed characters for url to check is 50.')
    else:
        status = True
        blacklist = ['localhost', '127.0.0.1', '11.10.10.77']
        url = ''.join(url)
        for b in blacklist:
            if b in url:
                status = False
                break
        if status == False:
            print('Sorry again, but this url is blacklisted.')
        else:
            proto, server, path, query, frag = parse.urlsplit(url)
            if query: path += '?' + query
            resp = urllib.request.urlopen(url)
            print(resp.read())
else:
    print("""
<!DOCTYPE html>
<html>
<h3>
This site simply does nothing, it just display whatever you want on browser.
<form method="get">
    <input name="url" placeholder="Gimme what you want to see...">
    <input type="submit" value="Show me the magic">
</form>
</html>
""" )