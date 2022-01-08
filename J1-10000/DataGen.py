import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

g = 9.8
fig, ax = plt.subplots()

def model_2pendulum(x,t):
    dtheta1dt = 6 * (2*x[2] - 3*np.cos(x[0] - x[1])*x[3]) / (16 - 9*np.power(np.cos(x[0] - x[1]),2))
    dtheta2dt = 6 * (8*x[2] - 3*np.cos(x[0] - x[1])*x[3]) / (16 - 9*np.power(np.cos(x[0] - x[1]),2))
    domega1dt = -1/2 * (x[0]*x[1]*np.sin(x[0] - x[1]) + 3*g*np.sin(x[0]))
    domega2dt = -1/2 * (-x[0]*x[1]*np.sin(x[0] - x[1]) + g*np.sin(x[1]))
    dzdt = [dtheta1dt, dtheta2dt, domega1dt, domega2dt]
    return dzdt

def model_2well(x,t):
    dxdt = x[1]
    dvdt = -(3*x[0]**3 - 2*x[0])
    return [dxdt, dvdt]

z0 = [1, 0]
t  = np.linspace(0, 10)

z  = odeint(model_2well, z0, t)

ax.plot(z[:,0], z[:,1])
plt.show()