# -*- coding:utf-8 -*- 
#@Time: 18-9-22 上午8:23
#@Author: Coast Cao

import numpy as np
import tensorflow as tf

print("#### set seed once ####")
np.random.seed(10)
tf.set_random_seed(1)

w = tf.Variable(tf.random_normal(mean=0., stddev=1., shape=()))
b = tf.Variable(tf.random_normal(shape=()))
sess = tf.Session()
sess.run(tf.global_variables_initializer())
for i in range(5):
    print("np random %d: %.3f" % (i,np.random.random()))
for i in range(5):
    print("tf random %d: w=%.3f" % (i,sess.run(w)))
for i in range(5):
    print("tf random %d: b=%.3f" % (i, sess.run(b)))

print("#### a fixed seed every time ####")
for i in range(5):
    np.random.seed(10)
    print("np random %d: %.3f" % (i, np.random.random()))

for i in range(5):
    tf.set_random_seed(10)
    print("tf random %d: w=%.3f" % (i, sess.run(w)))
for i in range(5):
    tf.set_random_seed(10)
    print("tf random %d: b=%.3f" % (i, sess.run(b)))

