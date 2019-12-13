'''
Verify if the given strings is an anagram.
Ex: Str1: LISTEN, Srt2: SILENT.
Alter the program if there is more than one letter that repeats in any one of the strings.
'''

from collections import Counter

def check_anagram(w1,w2):
    return Counter(w1) == Counter(w2)


w1 = 'LISTEN'
w2 = 'SILENT'
print(check_anagram(w1, w2))
