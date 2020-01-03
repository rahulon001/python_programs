"""
Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return
the shortest palindrome you can find by performing this transformation.

Input: "aacecaaa"
Output: "aaacecaaa"

"aabba"
"abcd"
"aacecaaa"

"""


# def shortestPalindrome(s: str) -> str:
#     s_list = list(s)
#     left_index = 0
#     right_index = len(s_list) - 1
#     while (left_index < right_index):
#         if s_list[left_index] != s_list[right_index]:
#             s_list.insert(left_index, s_list[right_index])
#             right_index += 1
#         elif checkForPalendrome(''.join(s_list)):
#             break
#         left_index += 1
#         right_index -= 1
#     return ''.join(s_list)

def shortestPalindrome(s: str) -> str:
    s_list = list(s)
    left_index = 0
    right_index = len(s_list) - 1
    while (left_index < right_index):
        if s_list[left_index] == s_list[right_index] and not checkForPalendrome(''.join(s_list)):
            s_list.insert(0, s_list[right_index])
            right_index += 1
        elif s_list[left_index] != s_list[right_index] and not checkForPalendrome(''.join(s_list)):
            s_list.insert(left_index, s_list[right_index])
            right_index += 1
        left_index += 1
        right_index -= 1
    return ''.join(s_list)

def checkForPalendrome(s):
    leftIdx = 0
    righIdx = len(s) - 1
    while (leftIdx < righIdx):
        if s[leftIdx] != s[righIdx]:
            return False
        leftIdx += 1
        righIdx -= 1
    return True


print(shortestPalindrome("aabba"))
print(shortestPalindrome("abcd"))
print(shortestPalindrome("aacecaaa"))
print(shortestPalindrome("abbabaab"))

"aabba"
"abcd"
"aacecaaa"



# k = 'kakkahsjj'
# print(list(k))
