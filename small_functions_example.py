from matplotlib.pyplot import*
from numpy import*

t = arange(0,1,0.01)
y1 = sin(2*pi*t)
y2 = 1.5*cos(3*pi*t)

def my_plot(t,y,fig_num = 1, x_label = 'Time(s)',y_label='',cl_fig=True):
	figure(fig_num)
	if cl_fig:
		clf()
	plot(t,y)
	if y_label:
		ylabel(y_label)

my_plot(t,y1,y_label = '$y_1(t)$')
my_plot(t,y2,y_label = '$y_2(t)$', fig_num = 2)
my_plot(t,y1+y2,y_label = '$y_1+y_2(t)$', fig_num = 3)
my_plot(t,y1-y2,y_label = '$y_1-y_2(t)$', fig_num = 4)

show()
