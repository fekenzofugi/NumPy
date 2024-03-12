# NumPy indexing
import numpy as np


arr = np.arange(1, 10)
print("Array to analize: {}".format(arr))

index = 8
print("The value in index {} is {}".format(index, arr[index]))

# slicing
slice = arr[0:5]
print("The sliced array is equal to {}".format(slice))

slice_beyond = arr[5:]
print("Array starting from index 5: {}".format(slice_beyond))

# assignment
slice_of_arr = arr[1:6]
print("The array from 1 to 6 is {}".format(slice_of_arr))
slice_of_arr[:] = 99
print("The array from 1 to 6 is {}".format(slice_of_arr))
# The original array changed too!!!
print("Array = {}".format(arr))

# copy()
arr_copy = arr.copy()
arr_copy_slice = arr_copy[1:6]
arr_copy_slice[:] = 10
print("Array copy = {}".format(arr_copy))
print("Array = {}".format(arr))

# 2d array
arr_2d = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print("Array to analyze: ".format(arr_2d))

# indexing
row_one_col_one = arr_2d[0, 0]
print("row 1, col 1 element: {}".format(row_one_col_one))

# slicing
arr_2d_slice = arr_2d[:2, 1:]
print("The slice is equal to:\n {}".format(arr_2d_slice))

first_section_slice = arr_2d[0:2, 0:2]
print("The slice is equal to:\n {}".format(first_section_slice))

# condicional
arr = np.arange(1, 11)
print(arr)

array_of_booleans = arr > 5
print(array_of_booleans)

# return the numbers > 5 -> conditional selection
print(arr[array_of_booleans])

# return numbers < 3
print(arr[arr < 3])
