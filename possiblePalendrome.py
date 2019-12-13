'''
possible palendrome
'''
import itertools

l = []
for s in list(map("".join, itertools.permutations("ccabdbacc"))):
    if s == s[::-1]:
        l.append(s)
print(set(l))