"""
Given a long sentence, reverse each word of the sentence individually in the sentence itself.
"""

def reverse_sentence(s):
    return ' '.join(word[::-1] for word in s.split(" "))

print(reverse_sentence("Geeks For Geeks is good to learn"))