import numpy as np
#Do not import any other libraries
"""
Write a function that takes 2 two dimensional arrays arr1 and arr2, and returns another two dimensional array. The resulting array should have the rows of
arr2 where the first element of each row is greater than zero, concatenated underneath the rows of arr1 where the first element of each row is greater than
zero. So for example, suppose

arr1 = array([[1,2,3.5,4],
              [3,-2,0,7],
              [0,8,-1,0]])

and arr2 = array([[-3,9,8.4,-11],
                  [0.5,-1,-1,-1],
                  [2,11,-3,-2.4]])

Then f(arr1,arr2) should return array([[ 1. ,  2. ,  3.5,  4. ],
                                       [ 3. , -2. ,  0. ,  7. ],
                                       [ 0.5, -1. , -1. , -1. ],
                                       [ 2. , 11. , -3. , -2.4]])
"""
def flmt(arr,r,num):
    return(arr[arr[:,r]>num, :])


def f(arr1, arr2):
    a1 = flmt(arr1,0,0)
    a2 = flmt(arr2,0,0)

    np.concatenate([a1,a2])
