# Introduction to Tensorflow

### 1 tensor
- 0-d number
- 1-d vector
- 2-d matrix

### 2 data flow graphs

```
graph LR
3-->a
5-->a
```

```python
import tensorflow as tf
a=tf.add(3,5)

print(a)
# Tensor("Add:0",shape=(),dtype=int32)

# get the value of a 
with tf.Session() as sess:
    print(sess.run(a))
    
```

### 3 more graphs

```
graph LR
x-->useless
add_op-->useless
x-->add_op
y-->add_op
add_op-->pow_op
x-->mul_op
y-->mul_op
mul_op-->pow_op
```

```python
import tensorflow as tf
x=2
y=3
add_op=tf.add(x,y)
mul_op=tf.multiply(x,y)
useless=tf.nultiply(x,add_op)
pow_op=tf.pow(add_op,mul_op)
with tf.Session() as sess:
    z=sess.run(pow_op)
    # 两个一起
    z,not_useless = sess.run([op3,useless])
    
```

### 4 Distributed Computation

```python
# Creates a graph.
with tf.device('/gpu:2'):
    a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], name='a')
    b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], name='b')
    c = tf.matmul(a, b)
    
# Creates a session with log_device_placement set to True.
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))

# Runs the op.
print(sess.run(c))

```


### 5 build more than one graph
```python
# to add operators to a graph, set it as default:
g = tf.Graph()
with g.as_default():
    x = tf.add(3, 5)
    
# add to graph
sess = tf.Session(graph=g)
with tf.Session() as sess:
    sess.run(x)
```

```python
# Do not mix default graph and user created graphs
g1 = tf.get_default_graph()
g2 = tf.Graph()
# add ops to the default graph
with g1.as_default():
    a = tf.Constant(3)
    
# add ops to the user created graph
with g2.as_default():
    b = tf.Constant(5)
```





