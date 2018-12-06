# Homework 1
# Tarik Dahnoun

# Computes the Riemenn Sum using midpoints

import numpy as np
import pylab as py

a = 0
b = np.pi / 2

N1 = 2
N2 = 4
N3 = 8
N4 = 16


def func(x):
    y = np.sin(x)
    return y


def analytic():
    return 1.0


A = analytic()


def midpoint(n):
    x = np.linspace(a, b, n, endpoint=False)
    I = np.zeros(n)
    dt = x[1] - x[0]

    for i in range(n):
        I[i] = func(x[i] + dt / 2) * dt
    I.tolist()
    II = sum(I)
    return II


I1 = midpoint(N1)
I2 = midpoint(N2)
I3 = midpoint(N3)
I4 = midpoint(N4)
print
"When N=", N1, "the sum is ", I1
print
"When N=", N2, "the sum is ", I2
print
"When N=", N3, "the sum is ", I3
print
"When N=", N4, "the sum is ", I4

error1 = abs(I1 - A)
error2 = abs(I2 - A)
error3 = abs(I3 - A)
error4 = abs(I4 - A)

count = 2
while abs(A - midpoint(count)) >= .002:  # plus or minus 10^-4
    count += 1
print
"It takes about", count, " time steps to be accurate to plus/minus 10^-4"

k = 1
while k <= 10:
    A = np.log10(midpoint(2 ** k) - 1)
    py.plot(np.log10(2 ** k), A, "r.-")
    k = k + 1

py.title("Error Vs N")
py.xlabel("log10(N)", fontsize=16)
py.ylabel("log10(error)", fontsize=16)
py.show()

print
print
"The error is proportional to the power of N"
print
"This value is 2, as shown on the slope of the graph."