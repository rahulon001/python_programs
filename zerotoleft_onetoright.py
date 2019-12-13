'''
Given a binary array {0,1,1,0,0,1,0,0,1} , sort the array in a way that all zeros come to the left and all the one's ' \
come to the right side of the array.
'''

def rearrange_bin(arr, n):
    i = -1
    for j in range(n):
        if arr[j] == 0:
            i += 1
            arr[i],arr[j] = arr[j], arr[i]
    print(arr)


arr = [0,1,1,0,0,1,0,0,1]
n = len(arr)
rearrange_bin(arr, n)