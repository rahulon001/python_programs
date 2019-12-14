"""Replace every element with the greatest element on right side"""

"""
Given an array of integers, replace every element with the next greatest element (greatest element on the right side) 
in the array. Since there is no element next to the last element, replace it with -1. For example, if the array is 
{16, 17, 4, 3, 5, 2}, then it should be modified to {17, 5, 5, 5, 2, -1}.
"""

def swap(arr, a, b):
    return arr[a], arr[b] == arr[b], arr[b]

def nextGreatest(arr):
    size = len(arr)
    max_from_right = arr[size - 1]
    arr[size - 1] = -1
    for i in range(size-2, -1, -1):
        temp = arr[i]
        arr[i] = max_from_right
        if max_from_right < temp:
            max_from_right = temp



# Utility function to print an array
def printArray(arr):
    for i in range(0, len(arr)):
        print(arr[i], end = ' ')


arr = [16, 17, 79, 3, 5, 2]
nextGreatest(arr)
printArray(arr)




