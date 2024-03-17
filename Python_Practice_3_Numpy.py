# -*- coding: utf-8 -*-
"""4299_Practice_3_Numpy

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dt3-W7Ejj0BfMpR4oB-hXNYmSnZRT__Z
"""

#2
import numpy as np

#3
lst = [1,2,3]
data = np.array(lst)
print(data)

#4
lst = [[1,2,3],[4,5,6]]
data = np.array(lst)
print(data)

#5
three_D = np.ones((2,3,4))
print(three_D)

#6
n_dim = np.array([1,2,3,4,5],ndmin=6)
print(n_dim)

#7
zeros = np.zeros((3,3))
print(zeros)

#8
ones = np.ones((3,3))
print(ones)

#10
empty = np.empty((4,3))
print(empty)

#11
arr = np.arange(1,6)
print(arr)

#12
arr_1 = np.linspace(0,10,5) # start ---- end ---- how much to be divided
print(arr_1)

#13
arr_sh = np.array([[1,2,3],[4,5,6]])
print(arr_sh.shape)

#14
arr_c = np.array([1,2,3,4,5])
print(arr_c.size)

#15
arr_d = np.array([[1,2,3]])
print(arr_d.ndim)

#16
arr_e = np.array([1,2,3,4,5])
arr_f = arr_e.astype('float64')
print(type(arr_f[0]))

#17
arr_e = np.array([1,2,3,4,5])
arr_f = arr_e.astype('float64')
arr_g = arr_f.astype('int64')
print(type(arr_g[0]))

#18
arr_h = np.array([3,7,1,8,4,6,0,2,5])
print('Max :',arr_h.max())
print('Min :',arr_h.min())

#19
arr = np.array([[1,2,3],[4,5,6]])
print(arr.reshape(3,2)) # must be a multiple of the no of elements in the array

#20
arr_split3 = np.array([1,2,3,4,5,6,7,8,9])
print(np.array_split(arr_split3,3))

#21
arr = np.array([[1,2,3,4],[4,5,6,7],[8,9,10,11],[12,13,14,15]])

#horizontal split
hori = np.hsplit(arr,2) #splits along axis = 1 ie column
print(hori)

#vertical split
verti = np.vsplit(arr,2) #splits along axis = 0 ie row
print(verti)

#22
arr = np.array([1,2,3,4])
two_D = arr[np.newaxis] #adds a new axis
print(two_D)

#this also adds a new dimension
#arr = np.array([1,2,3,4],ndmin=2)
#print(arr)

#23
arr_2D = np.array([[1,2,3],[4,5,6]])
print(arr_2D.flatten())

#24
arr = np.array([5,3,6,1,2,4])
sorted = np.sort(arr)
print(sorted)

#25
arr_1 = np.array([5,3,6,1,2,4])
arr_2 = np.array([1,7,8,5,6,8])
print(np.concatenate((arr_1,arr_2)))

#26
arr_1 = np.array([5,3,6,1,2,4])
arr_2 = np.array([1,7,8,5,6,8])
print(arr_1 + arr_2)

#27
arr_1 = np.array([5,3,6,1,2,4])
arr_2 = np.array([1,7,8,5,6,8])
print(arr_1 ** arr_2)

#28
arr = np.array([1,2,3])
print('Sum :',np.sum(arr))
print('Mean :',np.mean(arr))
print('Median :',np.median(arr))

#29
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
result = np.dot(A, B)
print(result)
print(A @ B)

#30
arr_2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_2D.transpose())

#32
arr_2D = np.array([[1,8,3],[4,7,6],[7,8,9]])
print(np.linalg.inv(arr_2D))

#34
# Create a NumPy array with missing values
arr = np.array([1, 2, np.nan, 4, 5])

# Check for missing values
has_missing_values = np.isnan(arr)

# Remove missing values
arr_cleaned = arr[~np.isnan(arr)]

# Replace missing values with 0
arr_replaced = np.nan_to_num(arr, nan=0)

print("Original Array:")
print(arr)

print("\nMissing Values:")
print(has_missing_values)

print("\nArray without Missing Values:")
print(arr_cleaned)

print("\nArray with Missing Values Replaced:")
print(arr_replaced)

#35
arr = np.array([1,2,3,4,5])
new_arr = np.where(arr > 2) # returns index of the values satisfying the condition
print(new_arr)
filtered_arr = arr[new_arr] #appends elements in that index to a new arr
print(filtered_arr)

#36
arr_1 = np.array([5,3,6,1,2,4])
arr_2 = np.array([1,7,8,5,6,8])
print(arr_1 * arr_2)

#37
arr_2D = np.array([[1,2,3],[4,5,6]])
print(arr_2D.ndim)
for i,val in enumerate(arr_2D,1):
  print(f'Mean of row {i} = {np.mean(val)}')
  print(f'Median of row {i} = {np.median(val)}')

#38
arr_1 = np.array([5,3,6,1,2,4])
print(f'STD DEV :{np.std(arr_1)}')

#39
arr = np.array([1,2,3,4,5])
arr_1 = np.array([1,2,3,4,5])
view_arr = arr.view()
copy_arr = arr_1.copy()
copy_arr[0]=10 #if we change in copy no changes in original array
view_arr[0]=10 #if we try to change view elements original array also changes
print('Arr:',arr)
print('View:',view_arr)
print('\n')
print('Arr_1:',arr_1)
print('Copy:',copy_arr)

#40
arr = np.array([1,2,3,4,5])
print(arr[:3]) #prints first 3
print(arr[2:]) #from 2 to end of array

#41
arr = np.array([1,2,3,4,5])
index = np.where(arr==3)
print(index)

#42
arr = np.array([1,2,3,4,5])
print(arr[:3]) #from start to 2 nd element

#43
arr = np.array([1,2,3,4,5,6,7,8,9]) #select every 2nd element
print(arr[::2]) #change number for that no of skip

#44
arr_2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
#selection of rows => 0:2, selection of columns =>1 [rows,columns]
column = arr_2D[0:2, 1]
print(column)

#45
arr_2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_2D[::-1])

#46
arr_2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.diagonal(arr_2D))

#47
arr = np.array([10,20,30,40,50])
bool_arr = np.array([True,False,False,True,False])
new_arr = arr[bool_arr] #prints element where True and masks element where False
print(new_arr)

#48
arr = np.array([10,20,30,40,50])
new_arr = np.where(arr > 20)
print(arr[new_arr])

#50
arr_2d = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9],
                    [10, 11, 12]])

# Define a condition (e.g., values in the first column greater than 3)
condition = arr_2d[:, 0] > 3
selected_rows = arr_2d[condition]
print(selected_rows)

#52
arr_1 = np.array([True,False,True,False])
arr_2 = np.array([True,True,False,False])
print('AND:',np.logical_and(arr_1,arr_2))
print('OR:',np.logical_or(arr_1,arr_2))
print('NOT:',np.logical_not(arr_1))

#53
arr_1 = np.array([5,3,6,1,2,4])
arr_2 = np.array([1,2,3,1,4,10])
print(arr_1 / arr_2)

#54
arr = np.array([10,20,30,40,50,10,20,40,50,30,10])
print(np.unique(arr)) #prints unique elements without duplicates
print(np.unique(arr, return_index=True)[1]) #returns index of unique elements
print(np.unique(arr, return_counts=True))
unique_elements, counts = np.unique(arr, return_counts=True)
print("Unique elements and their counts:")
for element, count in zip(unique_elements, counts):
    print(f"{element}: {count}")

#55
arr_1 = np.array([1, 2, 3, 4, 5])
arr_2 = np.array([5, 4, 3, 2, 1])
correlation_matrix = np.corrcoef(arr_1, arr_2)
print(correlation_matrix)
correlation_coefficient = correlation_matrix[0, 1]

print("Correlation Coefficient:", round(correlation_coefficient))

#56
arr_1 = np.array([1, 2, 3, 4, 5])
for i in arr_1:
  print(i)

#57
arr_1 = np.arange(1,21)
arr_2 = np.linspace(5,15,5)
print(arr_2)

#58
arr_1 = np.array([1, 2, 3, 4, 5])
arr_2 = np.array([5, 4, 3, 2, 1])
manhattan_distance = np.sum(np.abs(arr_1 - arr_2))
print(manhattan_distance)

#59
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr.flatten())

#60
arr = np.array([1,2,3,np.nan,4])
print(np.isnan(arr)) # result will be true if nan is presnt in the array

#61
arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(np.linalg.matrix_rank(arr))

#62
arr_1 = np.array([6,1,4,2,9,8,7,6])
sorted = np.sort(arr_1)
print(sorted[::-1])

#63
arr_3d = np.array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    [[19, 20, 21], [22, 23, 24], [25, 26, 27]]
])

arr_2D = arr_3d[:2,:2,:2]
print(arr_2D)

#64
arr_1 = np.array([6,1,4,2,9,8,7,9,10])
sorted = np.sort(arr_1)
print(sorted)
n = len(sorted)

if int(n%2)==1:
  print('Median:',sorted[int(n/2)])
else:
  med = (sorted[int((n/2)-1)] + sorted[int(n/2)])/2
  print('Median:',med)

#65
arr1 = np.array([[1, 2],
                  [3, 4]])
arr2 = np.array([[5, 6],
                  [7, 8]])

# axis 2 is not there so create a newaxis and concatnate on axis 2
result = np.concatenate((arr1[:, :, np.newaxis], arr2[:, :, np.newaxis]), axis=2)
print(result)