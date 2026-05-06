import matplotlib.pyplot as plt
import numpy as np
import math
# x = np.linspace(0,10,100)
x = []
for i in range(100):
    x.appen(i/10)
#print(x)
#y = np.sin(x)
y = []
for i in range(100):
    y.append(math.sin(x[i]))

print(y)
plt.plot(x,y)

plt.title("Grafica del Seno")
plt.show()
