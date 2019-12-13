'''

Verify if S2 = {5,8,2} is a subset of S1 = {1,5,4,6,8,2} and S3 = {5,8,2,7} is not a subset of S1.
'''

def check_subset(s1, s2):
    result = set(filter(lambda x: x in s1, s2))
    if len(result) != len(s2):
        print(False)
    else:
        print(True)

s1 = {1,5,4,6,8,2}
s2 = {5,8,2}
check_subset(s1,s2)

