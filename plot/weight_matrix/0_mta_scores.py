import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)

fig, ax = plt.subplots()

image = np.random.uniform(size=(10, 10))
image = [[0.7, 0.2, 0.00001, 0.000006, 0.0002],
         [0.1, 0.8, 0.05, 0.00003, 0.0006],
         [0.1, 0.2, 0.5, 0.1, 0.03],
         [0.06, 0.1, 0.2, 0.6, 0.2],
         [0.002, 0.001, 0.3, 0.1, 0.6]]
image = np.array(image, dtype=np.float32)
im = ax.imshow(image, cmap=plt.cm.gray.reversed())
ax.set_title('MTA weight matrix')

# Move left and bottom spines outward by 10 points
ax.spines.left.set_position(('outward', 2))
ax.spines.bottom.set_position(('outward', 2))
# Hide the right and top spines
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
# Only show ticks on the left and bottom spines
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

fig.colorbar(im, ax=ax)

plt.show()
