'''
Write a code to return a value 'True' if the number '1' throughout the array appears consecutively. Ex: S = {1,1,1,0,0,3,4}.
Else, return 'False' if the array does not have the given number (char = '1' in this case) in the consecutive order. Ex: S = {1,1,0,0,1,3,4}
'''
from collections import Counter

def check_consecutive_ones(arr):
    f = Counter(arr)[1]
    c,c1 = 0, 0
    for i in range(len(arr)):
        if arr[i] != 1:
            c += 1
        else:
            break

    for j in range(c, len(arr)):
        if arr[j] == 1:
            c1 += 1
        else:
            break

    if c1 == f:
        return True
    else:
        return False


arr = [0,1,1,0,0,0,0]
print(check_consecutive_ones(arr))
