1. # Fun with Tensorboard 

```python
# run tensorboard Lecture2.py

import tensorflow as tf
a=tf.constant(2,name="a")
b=tf.constant(3,name="b")
x=tf.add(a,b,name="add")

with tf.Session() as sess:
    writer = tf.summary.FileWriter("./graphs", sess.graph)
    print(sess.run(x))

writer.close()

```
and then
```
python Lecture.py
tensorboard --logit="./graphs"
```
2. # Constant types
##### Basic types
- tf.constant(value,dtype=None,shape=None,name='Const',vertify_shape=False)
```python
# create of 1d tensor
a.tf.constant([2,2],name="vector")
# create of 2x2 tensor(matrix)
b=tf.constant([[0,1],[2,3]],name="b")
```
##### specific value
- tf.zeros(shape, dtype=tf.float32, name=None)

```python
# n行m列
tf.zero([2,3],tf.int32) ==> [[0,0,0],[0,0,0]]
```
- tf.zeros_like(input_tensor, dtype=None, name=None, optimize=True)
```pyhton
# input_tensor is [[0,1],[2,3],[4,5]]
tf.zero_like(input_tensor) ==> [[0,0][0,0][0,0]]
```
- tf.ones(shape, dtype=tf.float32, name=None)
- tf.ones_like(input_tensor, dtype=None, name=None, optimize=True)
- tf.fill(dim,value,name=None)
```python
tf.fill([2,3],8) ==> [[8,8,8],[8,8,8]]
```
##### constant that are sequences
```
tf.linspace(start,stop,num,name=None)

tf.linspace(10.0,13.0,4,name="linspace") ==> [10.0,11.0,12.0,13.0]
```

```
tf.range(start,limit=None,delta=1,dtype=None,name='range')

# 'satrt' is 3,'limit' is 18,'delta' is 3
tf.range(start,limit,delta) ==> [3,6,8,12,15]

# 'satrt' is 3,'limit' is 1,'delta' is -0.5
tf.range(start,limit,delta) ==> [3,2.5,2,1.5]

# 'limit' is 5
tf.range(limit) ==> [0,1,2,3,4]
```

```python
for _ in np.linspace(0,10,4): # ok
for _ in tf.linspace(0,10,4): # Error

for _ in range(4): # ok
for _ in tf.range(4): # error
```

```python
tf.random_normal(shape, mean=0.0, stddev=1.0, dtype=tf.float32, seed=None, name=None)
tf.truncated_normal(shape, mean=0.0, stddev=1.0, dtype=tf.float32, seed=None,
name=None)
tf.random_uniform(shape, minval=0, maxval=None, dtype=tf.float32, seed=None,
name=None)
tf.random_shuffle(value, seed=None, name=None)
tf.random_crop(value, size, seed=None, name=None)
tf.multinomial(logits, num_samples, seed=None, name=None)
tf.random_gamma(shape, alpha, beta=None, dtype=tf.float32, seed=None, name=None)
```


3. # Math Operations
```
a = tf.constant([3, 6])
b = tf.constant([2, 2])
tf.add(a, b) # >> [5 8]
tf.add_n([a, b, b]) # >> [7 10]. Equivalent to a + b + b
tf.mul(a, b) # >> [6 12] because mul is element wise
tf.matmul(a, b) # >> ValueError
tf.matmul(tf.reshape(a, shape=[1, 2]), tf.reshape(b, shape=[2, 1])) # >> [[18]]
tf.div(a, b) # >> [1 3]
tf.mod(a, b) # >> [1 0]
```

4. # Data Types
##### Python Native Types
```python
# 0-d
tf.zero_like(t_0) # ==> 0
tf.ones_like(t_0) # ==> 0

# 1-d
t_1=[b"a",b"b",b"c"]
tf.zeros_like(t_1) # ==> ['','','']
tf.ones_like(t_1) # ==> Error

# 2-d
t_2=[[True,False,False],
     [True,False,False],
     [True,False,False]]

tf.zeros_like(t_2) # ==> 2x2 tensor,all element are False
tf.ones_like(t_2) # ==> 2x2 tensor,all element are True
```



5. # Variables

1.A constant is constant. A variable can be assigned to, its value can be changed.
2.A constant's value is stored in the graph and its value is replicated wherever the graph is loaded. A variable is stored separately, and may live on a parameter server.
```python
# create variable a with scalar value
a = tf.Variable(2, name="scalar")

# create variable b as a vector
b = tf.Variable([2, 3], name="vector")

# create variable c as a 2x2 matrix
c = tf.Variable([[0, 1], [2, 3]], name="matrix")

# create variable W as 784 x 10 tensor, filled with zeros
W = tf.Variable(tf.zeros([784,10]))
```
##### some ops
```
tf.Variable holds several ops:
x = tf.Variable(...)
x.initializer # init op
x.value() # read op
x.assign(...) # write op
x.assign_add(...) # and more
```

##### initialize
```python
# The easiest way is initializing all variables at once:
init = tf.global_variables_initializer()
with tf.Session() as sess:
sess.run(init)

# Initialize only a subset of variables:
init_ab = tf.variables_initializer([a, b], name="init_ab")
with tf.Session() as sess:
sess.run(init_ab)

# Initialize a single variable
W = tf.Variable(tf.zeros([784,10]))
with tf.Session() as sess:
sess.run(W.initializer)
```

##### tf.Variable.assign()
```python

W = tf.Variable(10)
W.assign(100)
with tf.Session() as sess:
sess.run(W.initializer)
print W.eval() # >> 10
--------
# 需要对W.assign进行运行,否则得不到正确的结果
# 此时不需要对W进行初始化，因为assign_op已经对此进行初始化了
W = tf.Variable(10)
assign_op = W.assign(100)
with tf.Session() as sess:
sess.run(W.initializer)
sess.run(assign_op)
print W.eval() # >> 100
```

##### 不同的session进行不同的初始化

```python
W = tf.Variable(10)

sess1 = tf.Session()
sess2 = tf.Session()

sess1.run(W.initializer)
sess2.run(W.initializer)

print sess1.run(W.assign_add(10)) # >> 20
print sess2.run(W.assign_sub(2)) # >> 8
```

##### Use a variable to initialize another variable
```python
# Want to declare U = 2 * W
# W is a random 700 x 100 tensor
W = tf.Variable(tf.truncated_normal([700, 10]))
U = tf.Variable(2 * W)

# Want to declare U = W * 2
# W is a random 700 x 100 tensor
W = tf.Variable(tf.truncated_normal([700, 10]))
U = tf.Variable(2 * W.intialized_value())

```

6. # Placeholders
- tf.placeholder(dtype, shape=None, name=None)

```python
# create a placeholder of type float 32-bit, shape is a vector of 3 elements
a = tf.placeholder(tf.float32, shape=[3])

# create a constant of type float 32-bit, shape is a vector of 3 elements
b = tf.constant([5, 5, 5], tf.float32)

# use the placeholder as you would a constant or a variable
c = a + b # Short for tf.add(a, b)

with tf.Session() as sess:
    # feed [1, 2, 3] to placeholder a via the dict {a: [1, 2, 3]}
    # fetch value of c
    print sess.run(c, {a: [1, 2, 3]})
# >> [6, 7, 8]
```
1. shape=None means that tensor of any shape will be accepted as value for placeholder.
2. shape=None is easy to construct graphs, but nightmarish for debugging.
3. shape=None also breaks all following shape inference, which makes many ops not work because they expect certain rank.

##### Feeding values to TF ops
```python
# create operations, tensors, etc (using the default graph)
a = tf.add(2, 5)
b = tf.mul(a, 3)

with tf.Session() as sess:
    # define a dictionary that says to replace the value of 'a' with 15
    replace_dict = {a: 15}
    
    # Run the session, passing in 'replace_dict' as the value to 'feed_dict'
    sess.run(b, feed_dict=replace_dict) # returns 45
```
6. # lazy loading

```python 
x = tf.Variable(10, name='x')
y = tf.Variable(20, name='y')

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    writer = tf.summary.FileWriter('./my_graph/l2', sess.graph)
    for _ in range(10):
        sess.run(tf.add(x, y)) # someone decides to be clever to save one line of code
    writer.close()
```
##### 初始化tensorboard
```
writer=tf.summary.FileWriter("./my_graph",sess.graph)
先运行文件 python lecture.py
tensorboard --logdir="my_graph"
```



