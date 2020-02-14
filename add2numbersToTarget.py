# two numbers sum

def twoNumberSum(array, target):
    nums = {}
    for num in array:
        potentialMatch = target - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []


def twoSum(array, target):
    array.sort()
    begin = 0
    end = len(array)-1
    while begin < end:
        currentSum = array[begin] + array[end]
        if currentSum == target:
            return [array[begin], array[end]]
        elif currentSum < target:
            begin += 1
        elif currentSum > target:
            end -= 1
    return []

print(twoSum([2,7,11,15], 9))