import os
import tensorflow as tf
from setting import *
from student_train import student

os.environ['CUDA_VISIBLE_DEVICES'] = select_gpu
gpuconfig = tf.ConfigProto(gpu_options=tf.GPUOptions(per_process_gpu_memory_fraction=per_process_gpu_memory_fraction))

# if not os.path.exists(checkpoint_dir):
#     os.makedirs(checkpoint_dir)
# if not os.path.exists(Savecode):
#     os.makedirs(Savecode)

with tf.Session(config=gpuconfig) as sess:
    model = student(sess)
    model.train() if phase == 'train' else model.test('test')
