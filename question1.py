import numpy as np
#Do not import any other libraries
"""
Write a function that takes a number n as input and returns a 2 dimensional array of size nxn
where the returned array has the following form.

f(1) returns array([[1]])
f(2) returns array([[2,1],
            `       [1,1]])
f(3) returns array([[3,2,1],
                    [2,2,1],
                    [1,1,1]])
f(4) returns array([[4,3,2,1],
                    [3,3,2,1],
                    [2,2,2,1],
                    [1,1,1,1]])

And so on.
Hint:
it is possible to add to a subset of an array.
For example, say arr = np.zeros(4). Then if you run arr[:2] = arr[:2] + np.array([1,2])
and print arr, array([1,2,0,0]) would be outputed.
Make sure you are returning a numpy array and not a list of lists.
"""

def f(n):
    ##########YOUR CODE HERE##########
    arr = np.zeros((n,n))
    b = np.zeros((n,n))

#initialize
    arr[0] = np.arange(n,0,-1)

    for i in range(n):
        b[i,:i]=1

        if i>0:
            arr[i] = arr[i-1] - b[i]

    return arr

    ###########END CODE###############
