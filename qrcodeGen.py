import qrcode
import pyzbar.pyzbar as pyzbar
from PIL import Image

# 生成二维码
def Genqrcode(url):
    img = qrcode.make(url)
    return img

def Deqrcode(img):
    qr = Image.open(img)
    barcodes = pyzbar.decode(qr)
    for barcode in barcodes:
        barcodeData = barcode.data.decode("utf-8")
    return barcodeData

if __name__ == "__main__":
    TestLink = "https://www.baidu.com"
    img = Genqrcode(TestLink)
    img.save("test.png")
    print(Deqrcode("alipay.jpg"))