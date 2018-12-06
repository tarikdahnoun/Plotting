# Homework P1
# Tarik Dahnoun
# 9/5/17

import numpy as n
import pylab as p


def sine(x):  # returns sin(1/x)
    return n.sin(1 / x)


b = n.arange(.1, 2, .1)
a = sine(b)

print(a[9])  # corresponds to x=1

# Graph
p.plot(b, a, "r")
p.plot(b, a, "r.")
p.title("Graph of sin(1/x)")
p.xlabel("x", fontsize=16)
p.ylabel("y", fontsize=16)
p.show()
p.savefig("Graphhw.pdf")