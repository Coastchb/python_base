import numpy as np
import matplotlib.pyplot as plt


# set x and y values
x = [6,9,13,20];
y = [23.04,23.05,22.96,23.02]
base_y=23.93;
TDNN_x=6;
TDNN_y=22.74;

# set the title and labels
plt.title("Performance on Mirror201703");
plt.xlabel("epochs");
plt.ylabel("CER(%)");

# set the scales
plt.axis([5,25,15.9,24.0]); # set the total length of axis
plt.xticks(x)   # show the scale

# plot the lines
plt.figure(1);
#plt.subplot(131);
plt.plot(range(5,25),[base_y]*20,'r--'); #, label="general")
plt.plot(x, y, 'bo:'); #, label="adapted(GMM lattice)")
plt.plot(6,TDNN_y,'kv'); #, label = "adapted(TDNN lattice)")
#plt.legend(loc='upper right')

# add text to dot
plt.text(5,base_y,"%.2f%%"%base_y,horizontalalignment='left',verticalalignment='top');
for xx,yy in zip(x,y):
    plt.text(xx,yy,"%.2f"%yy,horizontalalignment='left',verticalalignment='bottom');
plt.text(5,TDNN_y,"%.2f%%"%TDNN_y,horizontalalignment='left',verticalalignment='top')
#plt.subplot(132);

plt.show()
