from random import randint
from PIL import Image, ImageFont, ImageDraw, ImageFilter


def rndChar():
    return chr(randint(65, 90))


def rndColor():
    return randint(64, 255), randint(64, 255), randint(64, 255)


def rndColor2():
    return randint(32, 127), randint(32, 127), randint(32, 127)


def fontSize():
    return randint(20, 40)


width = 4*60
height = 60
im = Image.new('RGB', (width, height), (255, 255, 255))
fontPath = r'C:\Users\lenovo\Desktop\iTunes Crash Logs\Arial.ttf'

draw = ImageDraw.Draw(im)
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
for i in range(4):
    font = ImageFont.truetype(fontPath, fontSize())
    draw.text((i*60 + 10, 10), rndChar(), fill=rndColor2(), font=font)
im = im.filter(ImageFilter.BLUR)
im.save('code.jpg', 'jpeg')