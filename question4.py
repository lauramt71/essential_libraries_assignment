import numpy as np
#Do not import any other libraries
"""
Write a function that takes 2 one dimensional arrays and returns the cosine similarity between the arrays. The cosine similarity is defined as
the dot product between the 2 arrays where each array has been divided by its magnitude. The magnitude is the defined as the square root of the
sum of the squares of the elements. So the cosine similarity of arrays arr1 and arr2 is DotProduct(arr1/magnitude(arr1), arr2/magnitude(arr2)).
Round your answer to 4 decimal places. Suppose arr1 = array([1,2,3]) and arr2 = array([-4,0,3.5]). Then f(arr1, arr2) should return 0.3268
"""

def fmag(arr):
        mag = np.sqrt(np.sum(arr ** 2))
    return mag


def f(arr1, arr2):
    ##########YOUR CODE HERE##########
arr1 = np.array([1,2,3])
arr2 = np.array([-4,0,3.5])

return(np.dot(arr1/fmag(arr1),arr2/fmag(arr2)))

    ###########END CODE###############
