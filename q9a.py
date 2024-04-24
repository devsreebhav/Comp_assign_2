import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp 
"""
y=|y1|=|*************|
  |y2| |*************|
"""
h=0.001
x=np.arange(1,2+h,h)
n=x.size

def solution(x):
	return np.log(x)
	
"Function"
def fun(x,y):
	 return np.vstack((y[1], -np.exp(-2*y[0])))


"Residuals of bondary condition"	 
def bc(ya, yb):
	return np.array([ya[0], yb[0]-np.log(2)])
	
y=np.zeros((2,x.size))
y[0,0]=0
y[0,n-1]=np.log(2)

sol = solve_bvp(fun, bc, x, y)


x_plot = np.linspace(1, 2, 100)
y_plot = sol.sol(x_plot)[0]
plt.plot(x_plot, y_plot,label="From scipy.integrate solve_bvp ")
plt.plot(x_plot,solution(x_plot),"o",label="Analytic Solution")
plt.xlabel("$x$",fontsize=20)
plt.ylabel("y(x)",fontsize=20)
plt.legend()
plt.show()
