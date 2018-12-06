# -*- coding: utf-8 -*-
import pylab as py
import numpy as np
# # 
x = np.linspace(-5,5,100)  #Use these for accurate E field graph
y = np.linspace(-5,5,100)  #Use these for accurate E field graph       
            
                #I call it the Dahnoun Uncertainty Principle    
            
# x = np.linspace(-1,1,20)  #Use these for accurate potential graph
# y = np.linspace(-1,1,20)  #Use these for accurate potential graph


[X,Y] = np.meshgrid(x,y)
denominator1 = ((X)**2+(Y-.5)**2)**(3./2)
denominator2 = ((X)**2+(Y+.5)**2)**(3./2)


Ex = X / denominator1
Ey = (Y-.5) / denominator1

Ax=X / denominator2
Ay=(Y+.5) / denominator2

V1 = 1./np.sqrt(X**2+(Y-.5)**2)
V2 = 1./np.sqrt(X**2+(Y+.5)**2)

py.figure(1)

arrow_x = Ex-Ax
arrow_y = Ey-Ay
maximum_arrow_length = 10
arrows_too_big = np.sqrt(arrow_x**2 + arrow_y**2)>maximum_arrow_length
arrow_x[arrows_too_big] = 0
arrow_y[arrows_too_big] = 0
myfig = py.contour(X,Y,V2-V1,100)
myfig1=py.pcolor(X,Y,V2-V1,vmin=-10,vmax=10,cmap=py.cm.bwr)
py.quiver(X,Y,arrow_x,arrow_y, pivot="mid")
py.colorbar(myfig1)

EX= 1./((x-1.)**2) - 1./((x+1.)**2)
EY= (y-1.)/((y-1.)**2)**(3/2.) - (y+1.)/((y+1.)**2)**(3/2.)


py.figure(2)
py.plot(x,EX,"b")
py.plot(y,EY,"r")
py.ylim(-150,150)


py.show()
