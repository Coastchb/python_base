import numpy as np
import matplotlib.pyplot as plt


# set x and y values
x = [6,9,13,20];
y = [20.77,20.62,20.37,20.32]

# set the title and labels
plt.title("Performance on Mirror201704");
plt.xlabel("epochs");
plt.ylabel("CER(%)");

# set the scales
plt.axis([5,25,15.90,24.0]); # set the total length of axis
plt.xticks(x)   # show the scale

# plot the lines
plt.figure(1);
#plt.subplot(131);
plt.plot(range(5,25),[22.64]*20,'r--', label="general")
plt.plot(x, y, 'bo:', label="adapted(GMM lattice)")
plt.plot(6,20.38,'kv', label = "adapted(TDNN lattice)")
plt.legend(loc='upper right')

# add text to dot
plt.text(5,22.64,"22.64",horizontalalignment='right',verticalalignment='center');
for xx,yy in zip(x,y):
    plt.text(xx,yy,"%.2f"%yy,horizontalalignment='left',verticalalignment='bottom');
plt.text(6,20.38,"20.38%",horizontalalignment='left',verticalalignment='top')
#plt.subplot(132);

plt.show()
