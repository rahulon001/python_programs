def moveElementToEnd(array, toMove):
    # Write your code here.
    i = 0
    j = len(array) - 1
    while i < j:
        while i < j and array[j] == toMove:
            j -= 1
        if array[i] == toMove:
            array[i], array[j] == array[j], array[i]
        i += 1
    return array

print(moveElementToEnd([-1, -3, -7, 2, 4, 5, 6, 8, 9], 2))