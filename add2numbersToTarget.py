def twoSum(numbers, target):
    n = len(numbers)
    begin = 1
    end = n
    while begin < end:
        if numbers[begin -1] + numbers[end -1] == target:
            return [begin, end]
        elif numbers[begin - 1] + numbers[end - 1] > target:
            end -= 1
        else:
            begin += 1
    return -1

print(twoSum([2,7,11,15], 9))