import math

def printPowerSet(set, set_size):
    # set_size of power set of a set
    # with set_size n is (2**n -1)
    pow_set_size = (int)(math.pow(2, set_size))
    counter = 0
    j = 0
    # Run from counter 000..0 to 111..1


    # Driver program to test printPowerSet
    set = ['a', 'b', 'c']
    print(printPowerSet(set, 3))