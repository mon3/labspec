import numpy
import math as m
import pylab


x0=-5
delta_x=0.1
n_x=100
n=1
x1 = numpy.arange(x0, x0+n_x*delta_x, delta_x)


def first_derivative(x):
    return -2*x*m.exp(-x**2)


def function(x):
    return m.exp(-x**2)


def p_m(m_x, n_x1, delta_x1):
    if (m_x <= (n_x1/2)):
        return (2*m.pi*m_x)/(n_x1*delta_x1)
    else:
        return (2*m.pi*(m_x-n_x))/(n_x1*delta_x1)


func = []
for i in range(n_x):
    func.append(function(x0 + i*delta_x))

func = numpy.fft.fft(func)

func1 = []
for j in range(n_x):
    func1.append(func[j]*((p_m(j, n_x, delta_x)*1j)**n))

func = numpy.fft.ifft(func1)
pylab.plot(x1, func.real, '.')

fd = []
for k in range(n_x):
    fd.append(first_derivative(x1[k]))
pylab.plot(x1, fd)
pylab.show()
