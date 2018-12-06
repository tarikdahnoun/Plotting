import numpy as np

m=14.0 #kg
g=9.8 #m/s^2
l=1.2 #m
theta=35.0 #degrees
radian=35*np.pi/180 #35 degrees in radians

A=np.matrix([[1,0,-np.cos(radian)],[0,1,np.sin(radian)],[0,-l/2,l*np.sin(radian)/2]])
r=np.matrix([[0],[m*g],[0]])
v=np.linalg.solve(A,r)
print v