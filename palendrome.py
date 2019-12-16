def isPalendrome(string):
    reversedString = ""
    for i in reversed(range(len(string))):
        reversedString += string[i]
    return reversedString == string


def isPalendrome1(string):
    reversedString = []
    for i in reversed(range(len(string))):
        reversedString.append(string[i])

    return string == ''.join(reversedString)

def isPalendrome_recursively(string):
    leftIdx = 0
    righIdx = len(string)-1
    while(leftIdx < righIdx):
        if string[leftIdx] != string[righIdx]:
            return False
        leftIdx+=1
        righIdx-=1
    return True

def isPalendrome_best(string):
    leftIdx = 0
    righIdx = len(string)-1
    while(leftIdx < righIdx):
        if string[leftIdx] != string[righIdx]:
            return False
        leftIdx+=1
        righIdx-=1
    return True

print(isPalendrome_best("aba"))



import os
from os import path
import shutil

src = "C:\\Users\\****\\Desktop\\test1\\"
dst = "C:\\Users\\****\\Desktop\\test2\\"

files = [i for i in os.listdir(src) if i.startswith("CTASK") and path.isfile(path.join(src, i))]
for f in files:
    shutil.copy(path.join(src, f), dst)