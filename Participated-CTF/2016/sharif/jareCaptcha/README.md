#jareCaptcha

**Category:** WEB, PPC

Can you solve some sudoku challenges?

##Solution

In this challenge we are given a webpage with a sudoku table that we should solve and a captcha to protect page from being brute-forced.
Requested task is to solve the sudoku for 200 times and submit our results to get the flag.
Viewing source code of challenge, we will see that there is a javascript code for rendering sudoku table in client-side.

```javascript
function sudoku(w){
   var str
   str = "072106048410000000030874291090052386765080012203961405051390004320040107000000600";
   var j
   var a,b,l1,l2,l3,l4,t
   t="";
   l1="<td bgcolor=";
   l2=">&nbsp;&nbsp;</td>";
   l3="<td bgcolor=";
   l4="</td>";
   for (j=0;j<9;j++){
        if(j==0 | j==1 | j==2 | j==6 | j==7 | j==8){a="DDDDDD";b="FFFFFF";}
        if(j==3 | j==4 | j==5){b="DDDDDD";a="FFFFFF";}
        t+="<TR>";
        if (str.charAt(0+j*9)=="0"){t+=l1+a+l2;}else{t+=l3+a+">"+str.charAt(0+j*9)+l4;}
        if (str.charAt(1+j*9)=="0"){t+=l1+a+l2;}else{t+=l3+a+">"+str.charAt(1+j*9)+l4;}
        if (str.charAt(2+j*9)=="0"){t+=l1+a+l2;}else{t+=l3+a+">"+str.charAt(2+j*9)+l4;}
        if (str.charAt(3+j*9)=="0"){t+=l1+b+l2;}else{t+=l3+b+">"+str.charAt(3+j*9)+l4;}
        if (str.charAt(4+j*9)=="0"){t+=l1+b+l2;}else{t+=l3+b+">"+str.charAt(4+j*9)+l4;}
        if (str.charAt(5+j*9)=="0"){t+=l1+b+l2;}else{t+=l3+b+">"+str.charAt(5+j*9)+l4;}
        if (str.charAt(6+j*9)=="0"){t+=l1+a+l2;}else{t+=l3+a+">"+str.charAt(6+j*9)+l4;}
        if (str.charAt(7+j*9)=="0"){t+=l1+a+l2;}else{t+=l3+a+">"+str.charAt(7+j*9)+l4;}
        if (str.charAt(8+j*9)=="0"){t+=l1+a+l2;}else{t+=l3+a+">"+str.charAt(8+j*9)+l4;}
        t+="</TR>\n";
   }
   document.getElementById(w).innerHTML="<table style='text-align: center; vertical-align: middle; width: 270px; height: 270px;' border=2 cellpadding=0 cellspacing=0>\n"+t+"</table>\n";
}
```

Looking at javascript source we see that there is a variable named "str" that have the sudoko table's field values each time the page renders.
So the task is clear. we should first send a request to server, receive this value, solve this sudoku having "str" variable value and then send our result with captcha value.
But the tricky point is the captcha. Cause it's a little hard to crack this captcha each time.
Thanks to my teamtames that notices once a captcha is created for our session, we can access to it's value everytime we send a request with our session parameters.
It means that if we send a request to "http://ctf.sharif.edu:8084/jarecap?pool=images/&(\d*)" to generate a new captcha, We can send the value of this captcha
for unlimited times if we send requests with our session.

The python code for generate this process is given as below:

```python
from PIL import Image
import sys
import urllib
import json
import re
import requests


def findNextCellToFill(grid, i, j):
    for x in range(i,9):
        for y in range(j,9):
            if grid[x][y] == 0:
                return x,y
    for x in range(0,9):
        for y in range(0,9):
            if grid[x][y] == 0:
                return x,y
    return -1,-1


def isValid(grid, i, j, e):
    rowOk = all([e != grid[i][x] for x in range(9)])
    if rowOk:
            columnOk = all([e != grid[x][j] for x in range(9)])
            if columnOk:
                    # finding the top left x,y co-ordinates of the section containing the i,j cell
                    secTopX, secTopY = 3 *(i/3), 3 *(j/3)
                    for x in range(secTopX, secTopX+3):
                            for y in range(secTopY, secTopY+3):
                                    if grid[x][y] == e:
                                            return False
                    return True
    return False


def solveSudoku(grid, i=0, j=0):
    i,j = findNextCellToFill(grid, i, j)
    if i == -1:
        return True
    for e in range(1,10):
        if isValid(grid,i,j,e):
            grid[i][j] = e
            if solveSudoku(grid, i, j):
                return True
            # Undo the current cell for backtracking
            grid[i][j] = 0
    return False


def create_sudoku_list(s_str):
    r = []
    for i in range(len(s_str)/9):
        r.append([int(x) for x in s_str[9*i:9*i+9]])
    return r


def return_back_to_str(s_list):
    return ''.join([''.join([str(i) for i in x]) for x in s_list])


# s = requests.Session()
url = "http://ctf.sharif.edu:8084/"
cookies = dict(csrftoken='2lpf6Krl96cbpU5NLVKiqEOlANQ5uLJEwutMwSLzyg5oNMhwsUcnB1Farvic7uco',
               sessionid='xxs408hfkrfj73dpv4pvsdbwh5ku3m9e', PHPSESSID= 'qjp47pv1548uajdfhchddo5js3')


while True:
    r = requests.get(url, cookies=cookies)
    soup = BeautifulSoup(r.text, 'lxml')
    data  = soup.find_all("script")[0].string
    data = data.split('\n')[4]
    sudoku = data.split('"')[1]
    xx = create_sudoku_list(sudoku)
    result = solveSudoku(xx)
    solved = return_back_to_str(xx)
    csrftoken = str(r.headers).split('csrftoken=')[1].split(';')[0]
    post_data = {'csrfmiddlewaretoken': csrftoken,
                 'solvedsudoku': solved, 'captcha': 'HRU7CS6YL5', 'submit': 'Submit'}
    r = requests.post(url, data=post_data, cookies=cookies)
    print r.text
```

I also captured the values for csrf-token each time the page loads because of django-csrf-middleware-protection.
Because if we do'nt send this value within our requests, Django will raise an 403 forbidden exception. (And i know if i wrote my requests better, i can handle this problem with python easily... but we didn't have that much time to find the correct python code...:D)

& After 200 request's we get the flag in requests text data.