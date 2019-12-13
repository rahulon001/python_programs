'''
You are given 2 strings: string, strong. Find the common alphabets in two strings and print it.
i/p: string , strong
o/p: strng
'''
def common_alphabet(s1,s2):
    for a in s1:
        if a in s2:
            print(a)


common_alphabet('string', 'strong')
