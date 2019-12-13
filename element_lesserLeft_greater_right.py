'''
Given an array , find the element (say X) that has all the elements less that it to its left side and all the elements
greater to it on its right side.
The left and right elements of X need not be in sorted form.
'''

def pivote_element(arr, n):
    leftMax= [None]*n
    leftMax[0] = float('-inf')
    for i in range(1,n):
        leftMax[i] = max(leftMax[i-1], arr[i-1])
    rightMin = float('inf')
    for i in range(n - 1, -1, -1):
        if leftMax[i] < arr[i] and rightMin > arr[i]:
            return i
        rightMin = min(rightMin, arr[i])
    return -1


if __name__ == "__main__":
    arr = [2, 1, 4, 3, 6, 8, 10, 7, 9]
    n = len(arr)
    print("Index of the element is", pivote_element(arr, n))