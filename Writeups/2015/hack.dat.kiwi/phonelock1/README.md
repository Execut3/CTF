#Phonelock1

**Category:** Web

```python
import hashlib
salt="fcfc9dca66f3423a79dedd883726d842"
valid="22b8da7e3179107ecda49dc18fefe5dd"

password = 0
for i in range(9999):
    m = hashlib.md5()
    m.update(salt+str(i))
    if m.hexdigest() == valid:
        password = i
        
print "flag is = "+hashlib.md5(salt+str(password)+str(password)).hexdigest()
```