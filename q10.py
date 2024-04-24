"""
Adaptive RK
"""
import numpy as np
import matplotlib.pyplot as plt
import math


def f(t,y):
	return((y*y + y)/t)


def solution(t):
	return(2*t/(1-2*t))
	
t=1
b=3
w=-2
hmax=0.5
hmin=0.001
TOL=0.0001
y=np.ones(1)
x=np.ones(1)
y[0]=w
x[0]=t
flag=1
h=hmax
coun=0
while(flag==1):
	coun+=1
	K1=  h*f(t,w)
	K2 = h*f( t + h/4, w + K1/4)
	K3 = h*f( t + (3*h)/8, w + (3/32)*K1+(9/32)*K2)
	K4 = h*f( t + (12*h)/13, w + (1932/2197)*K1-(7200/2197)*K2+(7296/2197)*K3)
	K5 = h*f( t + h, w + (439/216)*K1-8*K2+(3680/513)*K3-(845/4104)*K4)
	K6 = h*f( t + h/2, w - (8/27)*K1+2*K2-(3544/2565)*K3+(1859/4104)*K4-(11/40)*K5)
	
	R=np.abs((1/360)*K1 - (128/4275)*K3 - (2197/75240)*K4 + (1/50)*K5 + (2/55)*K6)/h
	
		
	if(R<= TOL):
		t=t+h
		w=w + (25/216)*K1 + (1408/2565)*K3+(2197/4104)*K4-(1/5)*K5
		y=np.hstack((y,np.array([w]).reshape(1,)))
		x=np.hstack((x,np.array([t]).reshape(1,)))
	
	delta=0.84*((TOL/R)**(1/4))
	
	if(delta<=0.1):
		h=0.1*h
	elif(delta>=4):
		h=4*h
	else:
		h=delta*h
		
	if(h>hmax):
		h=hmax
		
	if(t>=b):
		flag=0
		
	elif(t+h>b):
		h=b-t
	elif(h<hmin):
		flag=0
		print("minimum h exceeded\nProcedure failed ")
	
	
x.reshape(coun,1)
y.reshape(coun,1)
plt.plot(x,y,"*r",label="Adaptive RK")
m=np.zeros(coun)
m=m-2.2
plt.plot(x,m,".b",label="Mesh")
x=np.arange(1,3+0.01,0.01)
plt.plot(x,solution(x),label="analytic solution")



#plt.plot(x,np.abs(solution(x)-y),label="Tolerence")
plt.legend()
plt.show()
