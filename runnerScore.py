'''
FInd the runner score from array.
'''
import heapq

def runner_score(arr, n):
    li = list(set(arr))
    heapq.heapify(li)
    #heapq is nlargest will give 2 largest value
    print(heapq.nlargest(2,li)[-1])

arr = [1,4,0,8,10,9,7]
n = len(arr)
runner_score(arr,n)