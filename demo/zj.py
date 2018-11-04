from PIL import Image
import numpy as np
import cv2

i = 0
j = 0

x1=int(input("Please intput x1:"))
y1=int(input("Please intput y1:"))

x2 = int(input("Please intput x2:"))
y2 = int(input("Please intput y2:"))


out = Image.open("free.jpg")#读取系统的照片
img=out.resize((256, 256))
img.convert('RGB')
#img.save("cut.jpeg")
width = img.size[0]#长度
height = img.size[1]#宽度

rectangle = np.zeros((height,width), dtype = "uint8")
#黑色区域的位置
cv2.rectangle(rectangle, (x1, y1), (x2, y2), 255, -1)

img1 = Image.fromarray(rectangle.astype('uint8')).convert('RGB')
print (img.size)#打印图片大小
print (img.getpixel((4,4)))
width = img.size[0]#长度
height = img.size[1]#宽度
for i in range(x1,x2):#遍历所有长度的点
    for j in range(y1,y2):#遍历所有宽度的点
        data = (img.getpixel((i,j)))
        img.putpixel((i,j),(0,0,0))#则这些像素点的颜色改成黑色
img.save("out2.jpeg")
img1.save("output.jpeg")
