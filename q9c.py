import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp 

h=0.001
x=np.arange(np.pi/4,np.pi/3+h,h)
n=x.size

def solution(x):
	return np.sqrt(np.sin(x))



"Function"
def fun(x,y):
	 return np.vstack((y[1], -(2*y[1]**3 + y[1]*y[0]**2)/np.cos(x) ))


" Residuals of bondary condition "	 
def bc(ya, yb):
	return np.array([ya[0]-2**(-1/4), yb[0]-0.5*12**(1/4)])
	
y=np.ones((2,x.size))


sol = solve_bvp(fun, bc, x, y)



y_plot = sol.sol(x)[0]
plt.plot(x, y_plot,label="From scipy.integrate solve_bvp ")
x=np.arange(np.pi/4,np.pi/3+h,10*h)
plt.plot(x,solution(x),".m",label="Analytic Solution")
plt.xlabel("$x$",fontsize=20)
plt.ylabel("y(x)",fontsize=20)
plt.legend()
plt.show()
