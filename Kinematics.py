#Homework 1
#Tarik Dahnoun
#8/31/17

import numpy as n
import pylab as p

g=9.8
t = n.linspace(0,10,5)

# v0 = raw_input("Insert initial velocity: ")
# v0=float(v0)
# theta= raw_input("Insert angle theta (degrees): ")
# theta=float(theta)
# theta = theta*n.pi/180
v0=100
theta= 45
theta = theta*n.pi/180

vx=v0*n.cos(theta)
vy=v0*n.sin(theta)

x = vx*t
y = vy*t - 0.5*g*t**2

print("The x-distances at times t={} are x={}" .format(t,x))
print("The y-distances at times t={} are y={}" .format(t,y))

#Graph
p.plot(x,y,"r")
p.plot(x,y,"r.")
p.title("Position Graph")
p.xlabel("x-position (meters)", fontsize=16)
p.ylabel("y-position (meters)", fontsize=16)
p.show()
p.savefig("Graphhw.pdf")