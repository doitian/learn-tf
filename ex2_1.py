import tensorflow as tf

a = tf.constant(1)
b = tf.constant(2)
c = a * b
d = a + b
f = c + d
e = d - c
g = f / e

with tf.Session() as sess:
    ans = sess.run(g)

print(ans)
