

def duplicate_character(st):
    string = {}
    for i in st:
        key = string.keys()
        if i in key:
            string[i] += 1
        else:
            string[i] = 1
    print(list(filter(lambda x: string[x] >= 2, [i for i in string.keys()])))


duplicate_character("yetiyet")