import numpy as np
import math
import matplotlib.pyplot as plt
h=0.01
yi1=math.e
yi2=1/3
y1=[yi1]
y2=[yi2]
ti=0
tf=1
n=(tf-ti)/h
t=[ti]

c=yi2
a=ti
b=yi1

def f(y,h,t):
  return (y/(1+9*h))

def g(y,h,t):
  l=(40*h*t-1+(160*h*h*t-80*h*t+1+80*h*y)**(1/2))/(40*h)
  return(l)

for i in range(1,math.ceil(n+1)):
  b=f(b,h,a)
  c=g(c,h,a)
  y1.append(b)
  y2.append(c)
  a=a+h
  t.append(a)

plt.plot(t, y1, color='g',  label='System 1')
plt.plot(t, y2, color='r',  label='System 2')
plt.ylabel("y")
plt.xlabel("t")
plt.title("Solution of the Initial Value Problems")
plt.legend()
plt.show()
