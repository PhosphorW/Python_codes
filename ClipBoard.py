import win32clipboard as wc
import time, os

def clearClipboard():
    wc.OpenClipboard()
    wc.EmptyClipboard()
    wc.CloseClipboard()

def getClipboard():
    # 获取剪贴板数据
    wc.OpenClipboard()
    if wc.EnumClipboardFormats():    # 数据格式不为 0，即剪切板是否为空
        data = wc.GetClipboardData(wc.CF_UNICODETEXT)
    else:
        data = False
    wc.CloseClipboard()
    return data

def writeFile(name, text):
    new_file = open(name, 'ab')
    new_file.write(text)
    new_file.close()

if __name__ == '__main__':
    clearClipboard()
    # 当剪切板有数据就执行操作
    while True:
        time.sleep(0.2)
        txt = getClipboard()
        if txt:
            print(txt)
            writeFile('./1.txt', bytes(txt,encoding='utf-8'))
            clearClipboard()