
# shift the letter "key" times ahead
def caesarCipherEncryptor(string, key):
    # Write your code here.
    result = ""
    for i in range(len(string)):
        char = string[i]
        if char.isupper():
            result += chr((ord(char)+ key-65) % 26 +65)
        else:
            result += chr((ord(char)+ key-97) % 26 +97)
    return result

print(caesarCipherEncryptor("abccd", 26))