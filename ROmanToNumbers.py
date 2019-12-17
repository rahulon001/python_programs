# Python program to convert Roman Numerals
# to Numbers
def value(s):
    if (s == 'I'):
        return 1
    if (s == 'V'):
        return 5
    if (s == 'X'):
        return 10
    if (s == 'L'):
        return 50
    if (s == 'C'):
        return 100
    if (s == 'D'):
        return 500
    if (s == 'M'):
        return 1000
    return -1

def romanToNumber(string):
    res = 0
    counter = 0
    while counter < len(string):
        s1 = value(string[counter])
        if (counter + 1 < len(string)):
            # Getting value of symbol s[i+1]
            s2 = value(string[counter + 1])

            # Comparing both values
            if (s1 >= s2):
                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s1
                counter = counter + 1
            else:
                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s2 - s1
                counter = counter + 2
        else:
            res = res + s1
            counter = counter + 1

    return res


print("Integer form of Roman Numeral is"),
print(romanToNumber("IVI"))