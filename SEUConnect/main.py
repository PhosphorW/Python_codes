import urllib
import http.cookiejar
import os
import re
import time
import base64

import sys
import SEUConnect
from PyQt5.QtWidgets import QApplication, QMainWindow


login_url = ''  # 登录post的URL
logout_url = ''  # 登出post的URL
info_url = ''  # 获取用户信息URL
info_name = 'user.ini'  # 存储账号密码

class ConnectWeb(object):
    def __init__(self):  # 获取保存的账号密码，若文件不存在则创建文件
        if os.path.exists(info_name):
            with open(info_name, 'r') as f:
                self.id = self.decrypt(f.readline().strip())
                self.pw = self.decrypt(f.readline().strip())
                ui.usrlineEdit.setText(self.id)
                ui.pwdlineEdit.setText(self.pw)
        else:
            with open(info_name, 'w') as f:
                pass
            self.id = ''
            self.pw = ''

    def set_id_pw(self, id, pw):  # 记录账号密码
        self.id = id
        self.pw = pw
        with open(info_name, 'w') as f:
            f.write('%s\n%s' % (self.encrypt(id), self.encrypt(pw)))

    def encrypt(self, s):  # 加密
        return base64.b32encode(base64.b64encode(s.encode('utf-8'))).decode('utf-8')

    def decrypt(self, s):  # 解密
        return base64.b64decode(base64.b32decode(s)).decode('utf-8')

    def isConnect(self):  # 检测目前是否联网
        try:
            with urllib.request.urlopen("http://www.baidu.com", timeout=2) as f:
            # with urllib.request.urlopen("w.seu.edu.cn", timeout=2) as f:
                if (f.status == 200):
                    return True
                else:
                    return False
        except:
            return False

    def showWifi(self): # 显示可用WIFI
        with os.popen("netsh wlan show networks mode=ssid | findstr \"SSID\"") as d:
            result = list()
            for line in d.readlines():  # 依次读取每行
                line = line.strip()  # 去掉每行头尾空白
                if not len(line) or line.startswith('#'):  # 判断是否是空行或注释行
                    continue  # 是的话，跳过不处理
                result.append(line[line.find(":")+2:])  # 保存
            # print(d.read())
            result.sort()
            return result

    def connect_wifi(self, name=None):  # 连接wifi
        os.system("netsh wlan connect name=%s" % name)

    def main(self): # 测试是否连接网络函数 for test
        if self.isConnect():
            print("is ok")
        else:
            print("is flase")

# 以下定义UI交互功能

def refresh_click():
    # ui.Button_refresh.setText("comfirm")
    ui.comboBox.clear()
    wifiRfresh = test.showWifi()
    ui.comboBox.addItems(wifiRfresh)

def usr_ok():
    test.set_id_pw(ui.usrlineEdit.text(),ui.pwdlineEdit.text())

def usr_clear():
    if os.path.exists(info_name):
        with open(info_name,'r+') as f:
            f.truncate()
    ui.usrlineEdit.setText('')
    ui.pwdlineEdit.setText('')

def auto_connect():
    if ui.comboBox.currentText() :
        # test.connect_wifi(ui.comboBox.currentText())
        print(ui.comboBox.currentText())
        print("connect")
        if ui.usrlineEdit.text() and ui.pwdlineEdit.text():
            print(ui.usrlineEdit.text())
            print("connect")
        else:
            print("请输入用户名或密码")
    else:
        print("请选择WiFi")

if __name__ == "__main__":

    # test.main()

    # 初始化窗口
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = SEUConnect.Ui_MainWindow()
    ui.setupUi(MainWindow)

    test = ConnectWeb()

    ui.Button_refresh.clicked.connect(refresh_click)
    ui.save_usr_btn.clicked.connect(usr_ok)
    ui.clear_usr_btn.clicked.connect(usr_clear)
    ui.connect_btn.clicked.connect(auto_connect)

    MainWindow.show()
    sys.exit(app.exec_())
