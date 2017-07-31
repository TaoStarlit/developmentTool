#coding: utf-8
import numpy as np
import matplotlib.pyplot as plt



y1 = [0.5]
y2 = [0.5]
z1 = [0.5]
z2 = [0.5]
i = 0


fs=18
ms=10

fig=plt.figure("random oscillo graph",edgecolor='r')

yplot=plt.subplot(1,2,1)
yplot.patch.set_facecolor('#222233')
plt.title('Y in a custom color',color='#aa00aa')
plt.ylabel("accelerometer",color='#aa00aa')
plt.xlim(0,20)
plt.ylim(0,1)
plt.grid(True)
plt.plot(y1,"r-",label="y1")#画y
plt.plot(y2,"b-",label="y2")#画y
plt.legend(bbox_to_anchor=(1, 1), loc='upper left', ncol=1)#(0.5,-0.1),下方居中 ncol分成几行



zplot=plt.subplot(1,2,2)
zplot.patch.set_facecolor('#333322')
plt.title('Z in a custom color',color='#00bb00')
plt.ylabel("gyroscope",color='#00bb00')
plt.xlim(0,20)
plt.ylim(0,1)
plt.grid(True)
plt.plot(z1,"g-",label="z1")#
plt.plot(z2,"c-",label="z2")#
plt.legend(bbox_to_anchor=(1, 1), loc='upper left', ncol=1)



plt.ion()#可交互地


import datetime
current = datetime.datetime.now()
with open('./data.csv', 'a') as f:
    f.write('\r\n\r\n'+str(current)+':\r\n')


while True:
    i += 1
    ty1=np.random.random()
    ty2=np.random.random()
    tz1=np.random.random()
    tz2=np.random.random()

    y1.append(ty1)#随机附在y后面
    y2.append(ty2)
    z1.append(tz1)#随机附在y后面
    z2.append(tz2)

    plt.subplot(1,2,1)
    if i>20:
        plt.xlim(i-20,i)#设置x当前的显示限制
    plt.plot(y1,"r-",label="y1")#画y
    plt.plot(y2,"b-",label="y2")#画y

    plt.subplot(1,2,2)
    if i>20:
        plt.xlim(i-20,i)#设置x当前的显示限制
    plt.plot(z1,"g-",label="z1")#画y
    plt.plot(z2,"c-",label="z2")#画y


    plt.pause(0.1)

    with open('./data.csv', 'a') as f:
        f.write('y: ,')
        f.write(str(ty1))
        f.write(',')
        f.write(str(ty2))
        f.write(',\t;\t,')
        f.write('z: ,')
        f.write(str(tz1))
        f.write(',')
        f.write(str(tz2))
        f.write(' \r\n')


'''
b: blue
g: green
r: red
c: cyan
m: magenta
y: yellow
k: black
w: white
'''