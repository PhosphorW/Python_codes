# -*- coding: utf-8 -*-
import os, base64


# pic转换为base64
def pic2base(img):
    with open(img, "rb") as f:
        # b64encode是编码，b64decode是解码
        base64_data = str(base64.b64encode(f.read()), encoding='utf-8')
        file = open('1.txt', 'wt', encoding='UTF-8')
        file.write(base64_data)
        file.close()


# base64转换为pic，file_name为待转换的base64文件
def base2pic(file_name):
    with open(file_name, "rb") as f:
        imgdata = base64.b64decode(str(f.read(), encoding='utf-8'))
        file = open('convert.jpg', 'wb')
        file.write(imgdata)
        file.close()


# 将大的txt文件拆分成指定字节数的小文件
def split(fname, file_size, fnumber):
    if os.path.exists(fname):
        i = 1
        a = open(fname, 'rb')
        while (i <= fnumber):
            file_name = '1_' + str(i) + '.txt'
            file_sp = open(file_name, 'wt', encoding='UTF-8')
            # sp = a.read(file_size)
            file_sp.write(str(a.read(file_size), encoding='UTF-8'))
            file_sp.close()
            # print(a.tell())
            i += 1
        a.close()


# 合并小文件
def combine(new_name, total_pack):
    new_file = open(new_name, 'ab')
    i = 1
    while (i <= total_pack):
        a = open('1_' + str(i) + '.txt', 'rb')
        new_file.write(a.read())
        a.close()
        i += 1
    new_file.close()


if __name__ == "__main__":
    pic2base("C:\\Desktop\\399996.png")
    fname = '1.txt'  # default为1.txt
    file_size = 10240*50  # 字节数，10240为10kb
    fnumber = os.path.getsize(fname) // file_size + 1  # 分块后的文件数量
    split(fname, file_size, fnumber)
    combine('2.txt', fnumber)
    base2pic('2.txt')
