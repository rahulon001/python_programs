"""
Given a string containing alphanumeric characters, calculate sum of all numbers present in the string.
"""
import re


def addNumbers(s):
    sum_ = 0
    s_list = re.split('[a-z]', s)
    for i in s_list:
        if i != '':
            sum_ += int(i)
    print(sum_)


def addNumbers1(s):
    s_list = sum(map(int, re.findall('\d+', s)))
    print(s_list)


def addNumbers2(s):
    # A temperory sterling
    temp = ""

    # hold sum of all numbers
    sum = 0
    for ch in s:
        if ch.isdigit():
            temp += ch
        else:
            sum += int(temp)

            # reset the temperory string
            temp = "0"
    # atoi(temp.c_str1()) takescare of trailing numbers
    print(sum + int(temp))


addNumbers("1abc23")
addNumbers1("12abc20yz68")
addNumbers2("12abc20yz68")
