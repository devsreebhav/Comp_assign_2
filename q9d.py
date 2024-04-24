import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp 

h=0.002
x=np.arange(0,np.pi+h,h)
n=x.size

def solution(x):
	return 2+np.sin(x)
	
"Function"
def fun(x,y):
	 return np.vstack((y[1], 1/2-y[1]**2/2 - y[0]*np.sin(x)/2 ))


" Residuals of bondary condition "	 
def bc(ya, yb):
	return np.array([ya[0]-2, yb[0]-2])
	
y=np.zeros((2,x.size))


sol = solve_bvp(fun, bc, x, y)



y_plot = sol.sol(x)[0]
plt.plot(x, y_plot,label="From scipy.integrate solve_bvp ")
x=np.arange(0,np.pi+h,10*h)
plt.plot(x,solution(x),".m",label="Analytic Solution")
plt.xlabel("$x$",fontsize=20)
plt.ylabel("y(x)",fontsize=20)
plt.legend()
plt.show()
