'''
Write a program to reveres string from intervals
'''

def reverse_string(st , interval):
    return st[:interval] + st[interval:][::-1]

print(reverse_string('test_string',4))