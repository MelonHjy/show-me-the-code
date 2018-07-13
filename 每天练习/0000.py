from PIL import Image, ImageDraw, ImageFont

img = Image.open(r'C:\Users\lenovo\AppData\Roaming\Tencent\QQ\Misc\316440458').convert('RGB')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(r'C:\Users\lenovo\Desktop\iTunes Crash Logs\Arial.ttf', 20)
w, h = img.size
# print(w,h)
draw.text((w*0.8, h*0.1), '4', font=font, fill='red')
img.save('change1.jpg','jpeg')
