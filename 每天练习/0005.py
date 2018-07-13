from PIL import Image


path = r'C:\Users\lenovo\PycharmProjects\aab\爬虫\image\1-'
for i in range(1, 13):
    img_path = path + str(i) + '.jpg'
    im = Image.open(img_path)
    # resize函数可以缩小，也可以放大
    # thumbnail只能缩小，不能放大
    im.resize((460, 644), Image.ANTIALIAS)
    new_path = r'C:\Users\lenovo\Desktop\新建文件夹\\' + str(i) + '.jpg'
    im.save(new_path, 'jpeg')
