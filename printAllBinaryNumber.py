for i in range(8):
    s = bin(i)[2:]
    print(s.zfill(3))

x = 8

a = map(lambda x : ['{:03b}'.format(i) for i in range(x)], ['a','b','c'])

print(list(a))