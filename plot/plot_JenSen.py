import numpy as np
import matplotlib.pyplot as plt


def y_fun(_x):
    return (_x-30)**2 - 10

# set x and y values
x = np.arange(1,50);
y = [y_fun(xx) for xx in x]
print(y)
plt.plot(x, y, 'b-')


a = 5
a_val = y_fun(a)
plt.plot([0,a,a],[a_val,a_val,-80],'r--')

b = 40
b_val = y_fun(b)
plt.plot([0,b,b],[b_val,b_val,-80],'r--')

mid = (a+b)/2
mid_val = y_fun(mid)
plt.plot([0,mid,mid],[mid_val,mid_val,-80],'r--')

plt.plot([a,b],[a_val,b_val],'r--')

EFX = (a_val + b_val)/2
plt.plot([0,mid,mid],[EFX,EFX,mid_val],'r--')


plt.xticks([a,b,mid], ["a","b","EX"])
plt.yticks([a_val,b_val,mid_val,EFX],["F(a)","F(b)","F(EX)","E(FX)"])
plt.axis([0,50,-80,1000]);
plt.show()




# set the title and labels
#plt.title("A");
#plt.xlabel("epochs");
#plt.ylabel("Accuracy(%)");

# set the scales
#plt.axis([0,20,30,100]); # set the total length of axis
#plt.xticks(x)   # show the scale

# plot the lines
#plt.figure(1);
#plt.subplot(131);
#plt.plot(range(5,25),[22.64]*20,'r--', label="general")
#plt.plot(x, y, 'bo:')
#plt.plot(x, y2, 'ro:', label='raw/evaluation')

#plt.plot(6,20.38,'kv', label = "adapted(TDNN lattice)")
#plt.legend(loc='uppper left')

# add text to dot
#plt.text(5,22.64,"22.64",horizontalalignment='right',verticalalignment='center');
#for xx,yy in zip(x,y):
#    plt.text(xx,yy,"%.2f"%yy,horizontalalignment='left',verticalalignment='bottom');
#plt.text(6,20.38,"20.38%",horizontalalignment='left',verticalalignment='top')
#plt.subplot(132);
