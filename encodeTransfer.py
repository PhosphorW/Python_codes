import chardet

def transfer(sourcefile, targetfile):
    f = open(sourcefile, 'r', errors='replace')
    text = f.read()
    f.close()
    f = open(targetfile, 'w', encoding='ascii', errors='replace')
    f.write(text)
    f.close()

path = "pad.sat"
f = open(path,'rb')
data = f.read()
print(chardet.detect(data))
# transfer("1", "1_transfer")