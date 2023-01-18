import datetime


infile = open('date.txt', 'r').readlines()
day = 5
res = 0

for i in infile:
    try:
        date = i.replace(',','').split(' ')
        #date1 = date[0][:3] + ' ' + date[1] + ' ' + date[2].strip()
        #date_object = datetime.datetime.strptime(date1, '%b %d %Y')
        #if date_object.weekday() == day:
        #    res += 1
        date = date[0][:3] + ' ' + date[1] + ' ' + str(int(date[2].strip())+1)
        date_object = datetime.datetime.strptime(date, '%b %d %Y')
        if date_object.weekday() == day:
            res += 1
    except:
        pass
print "ABCTF{%s}"%str(res)