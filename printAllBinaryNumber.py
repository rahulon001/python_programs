for i in range(8):
    s = bin(i)[2:]
    print(s.zfill(3))


['{:03b}'.format(i) for i in range(8)]