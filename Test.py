# this is just a test
import tensorflow as tf

print("hello word")

import this
import turtle

turtle.Pen.pensize(4)
turtle.Pen.pencolor('red')
turtle.__forwardmethods(100)


a=321
b=123
print(a/b)
print(a//b)
print(a%b)

a = 5
b = 10
c = 3
d = 4
e = 5
a += b
a -= c
a *= d
a /= e
print("a = ", a)

flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1
print("flag1 = ", flag1)
print("flag2 = ", flag2)
print("flag3 = ", flag3)
print("flag4 = ", flag4)
print("flag5 = ", flag5)
print(flag1 is True)
print(flag2 is not False)

f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))

f=0
c=(f-32)/1.8
print('%.1f华氏度=%1.f摄氏度' % (f,c))


import math
ra=1
le=2*ra*math.pi
s=math.pi*(ra**2)
print('周长是%.3f' % (le))
print('面积是%.4f' % (s))



year = 2012
# 如果代码太长写成一行不便于阅读 可以使用\或()折行
is_leap = (year % 4 == 0 and year % 100 != 0 or
           year % 400 == 0)
print(is_leap)


sum=0
for x in range(2,101,2):
    sum+=x
print(sum)



sum=0
for x in range(1,101):
    if x%2==0:
        sum+=x
print(sum)


import math as math

while True:
    num=int(input('请输入一个数字'))
    is_Need=False
    end=int(math.sqrt(num))
    for x in range(2,end+1):
        if num%x==0 and num!=1:
            is_Need=True
            break
    if is_Need:
        print('%d不是一个素数' % num)
    else:
        print('%d是一个素数' % num)


for x in range(10):
    print(x)



for x in range(100,1000):
    a=x//100
    b=x//10%10
    c=x%10
    if x==a**3+b**3+c**3:
        print(x)




import math
for x in range(2,10000):
    m=x//2
    sum=0
    for y in range(1,m+1):
        if x%y==0:
            sum+=y
    if sum==x:
        print(x)


for x in range(0,101):
    for y in range(0,101):
        if x+y+(100-5*x-3*y)*3==100 and 100-5*x-3*y>=0:
            print('公鸡%d只, 母鸡%d只, 小鸡%d只' % (x,y,(100-5*x-3*y)*3))


while True:
    num=int(input('请输入想要的数列的行数:'))
    if num==1:
        print(1)
    elif num>1:
        a1=1
        a2=1
        print(a1)
        print(a2)
        for x in range(2,num):
            print(a1+a2)
            temp=a2
            a2=a1+a2
            a1=temp