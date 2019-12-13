'''
Given two sorted arrays A and B that may have repeated elements. Form a new sorted array C that contains the elements of
 A and B [Condition : You are not allowed to merge the two arrays and then sort. ]
'''

def merge_two_arrays(a1,a2,n1,n2):
    result = [None]*(n1+n2)
    i, j, k = 0, 0, 0
    while i < n1 and j < n2:
        if a1[i] < a2[j]:
            result[k] = a1[i]
            i += 1
            k += 1
        else:
            result[k] = a2[j]
            j += 1
            k += 1
    while i < n1:
        result[k] = a1[i]
        i += 1
        k += 1
    while j < n2:
        result[k] = a2[j]
        j += 1
        k += 1

    for i in range(n1+n2):
        print(result[i], end=' ')


arr1 = [1, 3, 5, 7]
n1 = len(arr1)

arr2 = [2, 3, 6, 8]
n2 = len(arr2)
merge_two_arrays(arr1, arr2, n1, n2)
