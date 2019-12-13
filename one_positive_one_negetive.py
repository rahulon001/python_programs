'''
Given an array of positive and negative integers {-1,6,9,-4,-10,-9,8,8,4} (repetition allowed) sort the array in a way
such that the starting from a positive number, the elements should be arranged as one positive and one negative element
 maintaining insertion order. First element should be starting from positive integer and the resultant array should look
  like {6,-1,9,-4,8,-10,8,-9,4}
'''


def rearrange(arr,n):
    i = -1
    for j in range(n):
        if arr[j] < 0:
            i += 1
            print(i)
            arr[i], arr[j] = arr[j], arr[i]
    print(arr)

def rearrange_insertion_order(arr, n):
    i = 0
    for j in range(n):
        if arr[j] < 0:
            temp = arr[j]
            arr.remove(arr[j])
            arr.insert(i, temp)
            i += 1
    print(arr)

    pos, neg = i, 0
    while (pos < n and neg < pos and arr[neg] < 0):
        arr[neg], arr[pos] = arr[pos], arr[neg]
        pos += 1
        neg += 2

arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
n = len(arr)
rearrange_insertion_order(arr,n)
print(arr)

