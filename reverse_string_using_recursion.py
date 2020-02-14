def reverseStringUsingRecursion(string):
    if len(string) == 0:
        return
    temp = string[0]
    reverseStringUsingRecursion(string[1:])
    print(temp, end='')

string = "Geeks for Geeks"
reverseStringUsingRecursion(string)