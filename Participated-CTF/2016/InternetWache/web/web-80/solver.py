import zlib # A compression / decompression library
import glob, os

directory = '.git/objects'
os.chdir(directory)


def read_git_object(filename):
    compressed_contents = open(filename, 'rb').read()
    return zlib.decompress(compressed_contents)

result = []

for folder_name in glob.glob("*"):
    for file_name in glob.glob(folder_name+'/*'):
        try:
            filename = os.path.join(directory, file_name)
            data = read_git_object(filename)
            result.append(data)
        except:
            pass

flag = ''
for r in result:
    if 'IW{' in r:
        index = r.find('IW{')
        while True:
            flag += r[index]
            if r[index] == '}':
                break
            index += 1
            
    if flag:
        break
print 'flag is : %s'%flag