import random
from PIL import Image, ImageDraw
import skimage , math

print("Print the format of picture please: ")
k = str(input())
image = Image.open('test.'+k)
image = image.convert('L')
image.save('result.jpg')
width, height = image.size
print("Num of pixeles is:",width*height)
mass = [0]*16
for i in range(width):
    for j in range(height):
        pixelRGB = image.getpixel((i,j))
        mass[int((pixelRGB+1)/16)-1] +=1
for i in range(len(mass)):
    mass[i] = mass[i]/(width*height)
print(mass)
entro = 0
for i in range(0,16):
    if mass[i]!= 0:
        entro+= -mass[i]*math.log(mass[i],2)
print("Entropy of 16 groups (self-made function) is: "+str(entro))
print("Entropy of 256 groups (build-in function) is: "+str(skimage.measure.shannon_entropy(image,2)))
