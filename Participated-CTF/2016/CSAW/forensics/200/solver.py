from base64 import b64decode
import cv 

#load xml file
fileToLoad="position.out"
myLoadedData = cv.Load(fileToLoad)

#check data properties
print myLoadedData # this print shows matrix size, datatype, cool !

#access a cell of the matrix
# rowIdx=1
# colIdx=10
# print "Accessing matrix at col:"+str(colIdx)+", row:"+str(rowIdx)
# print myLoadedData[rowIdx, colIdx]


# in_file = open('booty', 'r').readlines()
# in_f = ''
# for i in in_file:
#     in_f += i.strip()
# result1 = b64decode(in_f)
# res_file = open('position.out', 'w')
# res_file.write(result1)
# res_file.close()
# 
# in_file = open('file', 'r').readlines()
# in_f = ''
# for i in in_file:
#     in_f += i.strip()
# result1 = b64decode(in_f)
# res_file = open('file.out', 'w')
# res_file.write(result1)
# res_file.close()
