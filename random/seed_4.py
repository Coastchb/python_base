# -*- coding:utf-8 -*-
# @Time		:2018/9/23 下午8:19
# @Author	:Coast Cao\

import tensorflow as tf
import matplotlib.pyplot as plt

tf.set_random_seed(-1)
a = tf.random_normal(())

vals = []
with tf.Session() as sess:
    for i in range(100000):
        vals.append(sess.run(a))


plt.title("value & frequency")
plt.xlabel('value')
plt.ylabel('frequency')
count, bins, ignored = plt.hist(vals, 30, normed=True)
#plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (bins - mu)**2 / (2 * sigma**2)), linewidth=2, color='r')
plt.show()
