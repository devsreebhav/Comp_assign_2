import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp 


h=0.001
x=np.arange(0,0.5*np.pi+h,h)
n=x.size
def solution(x):
	return np.exp(np.sin(x))

"Function"
def fun(x,y):
	 return np.vstack((y[1], y[1]*np.cos(x)-y[0]*np.log(y[0]) ))


" Residuals of bondary condition "	 
def bc(ya, yb):
	return np.array([ya[0]-1, yb[0]-np.exp(1)])
	
y=np.ones((2,n))

sol = solve_bvp(fun, bc, x, y)


x_plot = x
y_plot = sol.sol(x_plot)[0]
plt.plot(x_plot, y_plot,label="From scipy.integrate solve_bvp ")
x=np.arange(0,0.5*np.pi+h,25*h)
plt.plot(x,solution(x),"om",label="Analytic Solution")
plt.xlabel("$x$",fontsize=20)
plt.ylabel("y(x)",fontsize=20)
plt.legend()
plt.show()
