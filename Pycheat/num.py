#!/usr/bin/env python3
import numpy
import numpy as np
from math import pi

my_list = [1, 2, 3, 4]
my_array = np.array(my_list)
my_2darray = np.array([[1,2,3], [4,5,6]])

# Subset
my_array[1]

# Slice
my_array[0:2]

# Subset 2D Numpy arrays
my_2darray[:,0]

my_array > 3
my_array * 2
my_array + np.array([5,6,7,8])

