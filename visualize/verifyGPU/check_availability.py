
import sys
import tensorflow.keras
import pandas as pd
import sklearn as sk
import scipy as sp
import tensorflow as tf
import platform

gpu = len(tf.config.list_physical_devices('GPU'))> 0
print(gpu)