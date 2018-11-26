from numpy import *
import matplotlib.pyplot as plt
import math

def f(x):
    return x**cos(x**2)

x=linspace(1,10,250)

plt.plot(x,f(x),label='x^cos(x^2)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('zavdannja15.png',dpi=200)
plt.show()

