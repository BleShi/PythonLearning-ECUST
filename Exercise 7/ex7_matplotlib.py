import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,2*np.pi,10000)
y=np.cos(x)
plt.plot(x,y,"r--")
plt.show()