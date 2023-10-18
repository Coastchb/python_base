# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
import chardet


# coding=utf-8
def check_charset(file_path):
    import chardet
    with open(file_path, "rb") as f:
        data = f.read(4)
        charset = chardet.detect(data)['encoding']
        print('charset:{0}'.format(charset))
    return charset


scores = []

count = 0
for line in open('scores', encoding=check_charset('scores')).readlines():
    scores.append(eval(line.strip())[0][0][0][10:])

    count += 1
    if count >= 2000:
        break

# Fixing random state for reproducibility
np.random.seed(19680801)

fig, ax = plt.subplots()

image = np.mean(scores, axis=0)
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
