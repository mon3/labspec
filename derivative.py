import numpy as np
import pylab as plt
import matplotlib
import math
import cmath


def function(x):
	return math.exp(-x*x)


def momentum(m,n,delta_x):
	if (m<=n/2):
		return 2*cmath.pi*m/(n*delta_x)
	else:
		return 2*cmath.pi*(m-n)/(n*delta_x)

delta_x=0.01
n=1000
f_n = []
x_0=-5.0
x_vector= []

for i in range(n):
	print i
	x_vector.append(x_0+i*delta_x)
	f_n.append(function(x_0+i*delta_x))

f_m=np.fft.fft(f_n)

f_m_with_mom= []
derivative_nr=1
for k in range(n):
	#1-st derivative
	f_m_with_mom.append(f_m[k]*math.pow(momentum(k,n,delta_x),1)*1j)
	#2-nd derivative
	#f_m_with_mom.append(f_m[k]*math.pow(momentum(k,n,delta_x),2)*1j*1j)

#print f_m_with_mom

f_m_reverse=[]

f_m_reverse=np.fft.ifft(f_m_with_mom)

#print f_m_reverse*1/n

#result=sum(f_m_reverse/n)
plt.plot(x_vector,f_m_reverse.real)
plt.show()