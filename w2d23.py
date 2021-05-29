#~ yuzhou zhu_w2d2 3

from matplotlib.pyplot import*
from numpy import*

t = arange(0,1,0.01)
y = 2*sin(2*pi*t)

#~ Way 1

N = len(y)
y_sat1 = zeros(N)

for i in range(N):
    y_i = y[i]
    if -0.5 < y_i < 0.5 :
        y_sat1[i]=0
    elif y_i > 0.5:
        y_sat1[i]=y_i-0.5
    elif y_i<-0.5:
        y_sat1[i]=y_i+0.5
        
figure (1)
clf()
plot(t,y,'r--')
plot(t, y_sat1, label='$y(t)$',linewidth=2.0)
ylabel('$y(t)$')
xlabel('Time(sec.)')
legend(loc=1)

#~ Way 2

y_sat2 = zeros(N)
for i, y_i in enumerate(y):
    if -0.5 < y_i < 0.5 :
        y_sat2[i]=0
    elif y_i > 0.5:
        y_sat2[i]=y_i-0.5
    elif y_i<-0.5:
        y_sat2[i]=y_i+0.5

figure (2)
clf()
plot(t,y,'r--')
plot(t, y_sat2, label='$y(t)$',linewidth=2.0)
ylabel('$y(t)$')
xlabel('Time(sec.)')
legend(loc=1)

#~ Way 3

T = arange(0,1,0.01)
v0=[1 if s<0.5 else 0 for s in T]
v1=[1 if s>0.5 else 0 for s in T]
y1=(y-0.5)*v0
y2=(y+0.5)*v1

import copy
y_sat3_1 = copy.copy(y1)
y_sat3_2 = copy.copy(y2)

figure (3)
clf()
plot(t,y,'r--')
y_sat3_1 [y_sat3_1 < 0] = 0
y_sat3_2 [y_sat3_2 > 0] = 0

Y1 = y_sat3_1+y_sat3_2

plot(t,Y1, label='$y(t)$',linewidth=2.0)
ylabel('$y(t)$')
xlabel('Time(sec.)')
legend(loc=1)

#~ Way 4

import copy
y_sat4_1 = copy.copy(y1)
y_sat4_2 = copy.copy(y2)

figure (4)
clf()
plot(t,y,'r--')

inds1 = where(y1 < 0)[0]
y_sat4_1[inds1] = 0
inds2 = where(y2 > 0)[0]
y_sat4_2[inds2] = 0

Y2 = y_sat4_1+y_sat4_2

plot(t, Y2, label='$y(t)$',linewidth=2.0)
ylabel('$y(t)$')
xlabel('Time(sec.)')
legend(loc=1)

show()