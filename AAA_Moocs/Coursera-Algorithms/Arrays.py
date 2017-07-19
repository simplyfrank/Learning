import numpy as np

""""
Arrays can perform update, add and remove operations in constant time. 
They get expensive if add or remove is performed anywhere besides the end of the array.

The huge ADVANTAGE of Arrays is a constant time access to values for both read/write
"""

# Implementation of finding the index in a given array at a specific memory location
def calculate_array_idx(index, address= 1000, element_size = 8, first_index = 0):
    return address + element_size * (index - first_index)
print(calculate_array_idx(6))

# Multi-Dimensional Arrays
def calculate_mdimarray_idx(index, rows, cols, address=1000, element_size=8, first_index=0):
    #  extract the values for row and col from index
    idx_row, idx_col = index
    # Skip all rows up until the idx row, and the cells before the idx_col
    address += element_size * ((idx_row - 1) * cols + (idx_col - 1))
    return address
print(calculate_mdimarray_idx((3,4), 3,6))

# Adding an element at the end of an array


