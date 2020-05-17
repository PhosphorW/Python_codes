from PIL import Image, ImageDraw, ImageFont, ImageOps
import random


def write_letter_digit(image, char, posi_xy, size_wh, setfont, fillColor):
    # 生成字符大小的灰度图(指定w,h)，不指定color参数(默认黑色)
    img = Image.new('L', size_wh)
    img_draw = ImageDraw.Draw(img)

    # 将该单个字符写在灰度图上，fill=255表示白色
    img_draw.text((0, 0), char, font=setfont, fill=255)

    # 图像顺时针旋转90度，expand-扩展输出图像，使其足够大以容纳整个旋转图像
    img_rotate = img.rotate(-90, expand=True)

    # 给灰度图着色，黑色区域的填充色为(0,0,0)，白色区域的填充色为fillColor
    img_color = ImageOps.colorize(img_rotate, (0, 0, 0), fillColor)

    # 将img_color中的字符所在像素(掩码)粘贴到image上，box表示左上角的坐标(x,y)
    image.paste(img_color, box=posi_xy, mask=img_rotate)


def draw_text(image, fillColor, position, chars, setfont, draw):
    """
    将数个字符逐个按列写在图片上，并返回文字区域的坐标
    """
    char_interval = 3  # 文字间距
    char_interval_en = 0  # 英文文字间距
    left_top_x, left_top_y = position
    right_down_x, right_down_y = position
    for i, char in enumerate(chars):
        if i == 0:
            char_w, _ = setfont.getsize(char)
            right_down_x += char_w

        # 如果是数字字符或者字母字符，则需要旋转90度
        if ord(char) in ascll_alpnum:
            char_h, char_w = setfont.getsize(char)  # 因为字母数字是横着的，所以长宽互换
            right_down_y = right_down_y + char_h + char_interval_en
            posi_x, posi_y = left_top_x, right_down_y - char_h
            posi_xy, size_wh = (posi_x + 3, posi_y), (char_h, char_w)
            write_letter_digit(image, char, posi_xy, size_wh, setfont, fillColor)
        else:
            _, char_h = setfont.getsize(char)
            right_down_y = right_down_y + char_h + char_interval
            posi_x, posi_y = left_top_x, right_down_y - char_h
            draw.text((posi_x, posi_y), char, font=setfont, fill=fillColor)

            # return left_top_x, left_top_y, right_down_x, right_down_y + char_interval


# ascll_alpnum = list(range(48, 58)) + list(range(65, 91)) + list(range(97, 123))
ascll_alpnum = list(range(0, 127))

img = Image.open("C:\\Users\\cblph\\Desktop\\001.jpg")
chName = ""
enName = ""
white = (255, 255, 255)
black = (0, 0, 0)

draw = ImageDraw.Draw(img)
font1 = ImageFont.truetype('C:\\Windows\\Fonts\\simsun.ttc', 40)
font2 = ImageFont.truetype('C:\\Windows\\Fonts\\STSONG.TTF', 28)
# draw.text((0, 0), chName, fill=(0,0,0), font=font1)
draw_text(img, white, (5, 10), chName, font1, draw)
draw_text(img, white, (45, 19), enName, font2, draw)
# img.show()
saveName = "C:\\Users\\cblph\\Desktop\\" + chName + '-0' + str(random.randint(1, 9)) + "-venuseo.jpg"
img.save(saveName)
