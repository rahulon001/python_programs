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


def isPalendrome_best(string: str) -> bool:
    left_idx = 0
    right_idx = len(string) - 1
    while left_idx < right_idx:
        if string[left_idx] != string[right_idx]:
            return False
        left_idx += 1
        right_idx -= 1
    return True


if __name__ == "__main__":
    print(isPalendrome_best("aba"))

#
# import os
# from os import path
# import shutil
#
# src = "C:\\Users\\****\\Desktop\\test1\\"
# dst = "C:\\Users\\****\\Desktop\\test2\\"
#
# files = [i for i in os.listdir(src) if i.startswith("CTASK") and path.isfile(path.join(src, i))]
# for f in files:
#     shutil.copy(path.join(src, f), dst)
