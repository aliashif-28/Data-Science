import matplotlib.pyplot as plt
import numpy as np
a = [20,15,10,5]
b = [1,2,3,4]
c = [13,14,15,16]
d = [1,2,3,4]
x = (a,b)
y = (c,d)
plt.plot(x,y,'ro--')
plt.xlabel('a,b')
plt.ylabel('c,d')
plt.title('Random graph')
plt.show()