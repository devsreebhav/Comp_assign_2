"""
second order ode by RK4

let dy/dx=z=f(x,y,z)
    dz/dx=g(x,y,z)
"""
import numpy as np
import matplotlib.pyplot as plt

def f(x,y,z,v):
	return(y+2*z-2*v+np.exp(-x))
	
def g(x,y,z,v):
	return(z+v-2*np.exp(-x))

def h(x,y,z,v):
	return(y+2*z+np.exp(-x))
	
dx=0.01	
x=np.arange(0,1+dx,dx)	
n=x.size


y=np.zeros(n)
z=np.zeros(n)
v=np.zeros(n)
y[0]=3
z[0]=-1
v[0]=1
for i in range(0,n-1,1):
	k0=dx*f(x[i],y[i],z[i],v[i])
	l0=dx*g(x[i],y[i],z[i],v[i])
	m0=dx*h(x[i],y[i],z[i],v[i])
	
	k1=dx*f(x[i]+dx/2,y[i]+k0/2,z[i]+l0/2,v[i]+m0/2)
	l1=dx*g(x[i]+dx/2,y[i]+k0/2,z[i]+l0/2,v[i]+m0/2)
	m1=dx*h(x[i]+dx/2,y[i]+k0/2,z[i]+l0/2,v[i]+m0/2)
	
	k2=dx*f(x[i]+dx/2,y[i]+k1/2,z[i]+l1/2,v[i]+m1/2)
	l2=dx*g(x[i]+dx/2,y[i]+k1/2,z[i]+l1/2,v[i]+m1/2)
	m2=dx*h(x[i]+dx/2,y[i]+k1/2,z[i]+l1/2,v[i]+m1/2)
	
	k3=dx*f(x[i]+dx/2,y[i]+k2,z[i]+l2,v[i]+m2)
	l3=dx*g(x[i]+dx/2,y[i]+k2,z[i]+l2,v[i]+m2)
	m3=dx*h(x[i]+dx/2,y[i]+k2,z[i]+l2,v[i]+m2)
	
	y[i+1]=y[i]+(k0+2*k1+2*k2+k3)/6
	z[i+1]=z[i]+(l0+2*l1+2*l2+l3)/6
	v[i+1]=v[i]+(m0+2*m1+2*m2+m3)/6
	
	
plt.plot(x,y,".b",label="u1(t)")
plt.plot(x,z,".k",label="u2(t)")
plt.plot(x,v,".r",label="u3(t)")
plt.xlabel("$t$",fontsize=20)
plt.legend()
plt.show()
