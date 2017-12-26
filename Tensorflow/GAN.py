import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
import random
import pandas as pd

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.
x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))

n=120

x_train=x_train[0:n]
x_test=x_test[n:n+n]

noise_factor = 0.1
x_train_noisy = x_train + noise_factor * np.random.normal(loc=0.0, scale=1.0, size=x_train.shape) 
x_test_noisy = x_test + noise_factor * np.random.normal(loc=0.0, scale=1.0, size=x_test.shape) 

x_train_noisy = np.clip(x_train_noisy, 0., 1.)
x_test_noisy = np.clip(x_test_noisy, 0., 1.)

x_train_noisy=np.concatenate([x_train_noisy,x_train_noisy])
x_test_noisy=np.concatenate([x_test_noisy,x_test_noisy])
x_train=np.concatenate([x_train,x_train])

np.random.seed(200)
sel=random.sample(range(0,x_train.shape[0]), n)
x_train_noisy=x_train_noisy[sel]
x_test_noisy=x_test_noisy[sel]
x_train=x_train[sel]

y_train=y_train[0:n]
y_train=np.concatenate([y_train,y_train])[sel]
y_train=np.array(pd.get_dummies(y_train)).astype(np.float32)
y_test=y_test[0:n]
y_test0=np.concatenate([y_test,y_test])[sel]
y_test=np.array(pd.get_dummies(y_test0))

x_train=np.array(x_train).astype(np.float64)
x_train_noisy=x_train_noisy.astype(np.float64)

learning_rate = 0.002
batch_size = n

display_step = 50
examples_to_show = 10

num_hidden_1 = 256
num_hidden_2 = 256 
num_input = 784 

X = tf.placeholder("float", [None, num_input])
Y = tf.placeholder("float", [None, num_input])

weights = {
    'encoder_h1': tf.Variable(tf.random_normal([num_input, num_hidden_1])),
    'encoder_h2': tf.Variable(tf.random_normal([num_hidden_1, num_hidden_2])),
    'decoder_h1': tf.Variable(tf.random_normal([num_hidden_2, num_hidden_1])),
    'decoder_h2': tf.Variable(tf.random_normal([num_hidden_1, num_input])),
}
biases = {
    'encoder_b1': tf.Variable(tf.random_normal([num_hidden_1])),
    'encoder_b2': tf.Variable(tf.random_normal([num_hidden_2])),
    'decoder_b1': tf.Variable(tf.random_normal([num_hidden_1])),
    'decoder_b2': tf.Variable(tf.random_normal([num_input])),
}

def encoder(x):
    layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x, weights['encoder_h1']),
                                   biases['encoder_b1']))
    layer_2 = tf.nn.sigmoid(tf.add(tf.matmul(layer_1, weights['encoder_h2']),
                                   biases['encoder_b2']))
    return layer_2


def decoder(x):
    layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x, weights['decoder_h1']),
                                   biases['decoder_b1']))
    layer_2 = tf.nn.sigmoid(tf.add(tf.matmul(layer_1, weights['decoder_h2']),
                                   biases['decoder_b2']))
    return layer_2

encoder_op = encoder(X)
decoder_op = decoder(encoder_op)

y_pred = decoder_op
y_true = Y

loss = tf.reduce_mean(tf.pow(y_true - y_pred, 2))
optimizer = tf.train.AdamOptimizer(learning_rate).minimize(loss)


def next_batch(num, data, labels):
    idx = np.arange(0 , len(data))
    np.random.shuffle(idx)
    idx = idx[:num]
    data_shuffle = [data[ i] for i in idx]
    labels_shuffle = [labels[ i] for i in idx]
    return np.asarray(data_shuffle).astype(np.float32), np.asarray(labels_shuffle).astype(np.float32)





### LINK AUTOENCODER + CNN



num_classes=10
dropout = 0.75

keep_prob = tf.placeholder(tf.float32) # dropout

X2 = tf.placeholder("float", [None, num_input])
Y2 = tf.placeholder("float", [None, num_classes])

def conv2d(x, W, b, strides=1):
    x = tf.nn.conv2d(x, W, strides=[1, strides, strides, 1], padding='SAME')
    x = tf.nn.bias_add(x, b)
    return tf.nn.relu(x)


def maxpool2d(x, k=2):
    return tf.nn.max_pool(x, ksize=[1, k, k, 1], strides=[1, k, k, 1],
                          padding='SAME')

def conv_net(x, weights, biases, dropout):
    x = tf.reshape(x, shape=[-1, 28, 28, 1])
    conv1 = conv2d(x, weights['wc12'], biases['bc12'])
    conv1 = maxpool2d(conv1, k=2)
    conv2 = conv2d(conv1, weights['wc22'], biases['bc22'])
    conv2 = maxpool2d(conv2, k=2)
    fc1 = tf.reshape(conv2, [-1, weights['wd12'].get_shape().as_list()[0]])
    fc1 = tf.add(tf.matmul(fc1, weights['wd12']), biases['bd12'])
    fc1 = tf.nn.relu(fc1)
    fc1 = tf.nn.dropout(fc1, dropout)
    out = tf.add(tf.matmul(fc1, weights['out2']), biases['out2'])
    return out

weights2 = {
    'wc12': tf.Variable(tf.random_normal([5, 5, 1, 32])),
    'wc22': tf.Variable(tf.random_normal([5, 5, 32, 64])),
    'wd12': tf.Variable(tf.random_normal([7*7*64, 1024])),
    'out2': tf.Variable(tf.random_normal([1024, num_classes]))
}

biases2 = {
    'bc12': tf.Variable(tf.random_normal([32])),
    'bc22': tf.Variable(tf.random_normal([64])),
    'bd12': tf.Variable(tf.random_normal([1024])),
    'out2': tf.Variable(tf.random_normal([num_classes]))
}

logits = conv_net(X2, weights2, biases2, keep_prob)
prediction2 = tf.nn.softmax(logits)

loss_op2 = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
    logits=logits, labels=Y2))
optimizer2 = tf.train.AdamOptimizer(learning_rate=learning_rate)
train_op = optimizer2.minimize(loss_op2)

correct_pred2 = tf.equal(tf.argmax(prediction2, 1), tf.argmax(Y2, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred2, tf.float32))

init = tf.global_variables_initializer()

num_steps =4000


with tf.Session() as sess:
    sess.run(init)
    for i in range(1, num_steps+1):
        batch_x, batch_y=next_batch(batch_size, x_train_noisy, x_train)        
        _, l = sess.run([optimizer, loss], feed_dict={X: batch_x.reshape(n,784),
                        Y:batch_y})
        if i % display_step == 0 or i == 1:
            print('Epoch %i: Denoising Loss: %f' % (i, l))
        output=sess.run([decoder_op],feed_dict={X: x_train_noisy})
        x_train2=np.array(output).reshape(n,784).astype(np.float64)
        batch_x2, batch_y2 = next_batch(batch_size, x_train2, y_train)
        sess.run(train_op, feed_dict={X2: batch_x2.reshape(n,784), Y2: batch_y2, keep_prob: 0.8})
        if i % display_step == 0 or i == 1:
            loss3, acc = sess.run([loss_op2, accuracy], feed_dict={X2: batch_x2,
                                                                 Y2: batch_y2,
                                                                 keep_prob: 1.0})
            print("Epoch " + str(i) + ", CNN Loss= " + \
                  "{:.4f}".format(loss3) + ", Training Accuracy= " + "{:.3f}".format(acc))
    print('\n','Accuracy Train:',acc)

    output3=sess.run([decoder_op],feed_dict={X: x_test_noisy})
    x_test22=np.array(output3).reshape(n,784).astype(np.float64)

    output33 = sess.run([prediction2],feed_dict={X2:x_test22,keep_prob: 1.0})
    pred0=np.argmax(output33,axis=2)[0]

print('Accuracy Test:',1-np.count_nonzero(y_test0-pred0)/n)

np.where(np.array(sel)<100)


plt.figure(figsize=(7, 7))
ax = plt.subplot(1, 2, 1)
plt.imshow(x_test_noisy[2].reshape(28, 28))
plt.gray()
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
ax = plt.subplot(1, 2, 2)
plt.imshow(np.array(output3)[0].reshape(n,28, 28)[2])
plt.gray()
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()

