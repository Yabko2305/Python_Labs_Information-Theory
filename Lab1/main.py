import random
from PIL import Image
import skimage , math , numpy as np, cv2
import matplotlib.pyplot as plt

print("Print the format of picture please: ")
k = str(input())
image = Image.open('test.'+k)
image = image.convert('L')
image.save('result.jpg')
width, height = image.size
print("Num of pixeles is:",width*height)
mass = [0]*16
massforall = [0]*256
for i in range(width):
    for j in range(height):
        pixelRGB = image.getpixel((i,j))
        mass[int((pixelRGB+1)/16)-1] +=1
        massforall[pixelRGB]+=1
hista = list.copy(mass)
for i in range(len(mass)):
    mass[i] = mass[i]/(width*height)
print(mass)
entro = 0
for i in range(0,16):
    if mass[i]!= 0:
        entro+= -mass[i]*math.log(mass[i],2)
print("Entropy of 16 groups (self-made function) (format "+k+") is: "+str(entro))
print("Entropy of 256 groups (build-in function) (format "+k+") is: "+str(skimage.measure.shannon_entropy(image,2)))

print("Do u want to see histogram?")
if str(input()) == "yes":
    # гістограма 16 груп
    x = range(len(hista))
    ax = plt.gca()
    ax.bar(x, hista, align='edge')
    ax.set_xticks(x)
    ax.set_xticklabels([str(s) for s in range(1,17)])
    plt.show()
print("Do u want to see histogram of 256 groups?")
if str(input()) == "yes":
    # гістограма 256 груп
    x = range(len(massforall))
    ax = plt.gca()
    ax.bar(x, massforall, align='edge')
    ax.set_xticks(x)
    ax.set_xticklabels([str(s) if s %20 ==0 or s == 1 or s == 256 else " " for s in range(1,257) ])
    plt.show()





