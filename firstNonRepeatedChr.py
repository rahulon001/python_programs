def printFirstNonRepeatedCharacter(string):
    dictionary, lst = {}, []
    for character in string:
        key = dictionary.keys()
        try:
            if character in key:
                dictionary[character] = 0
                lst.remove(character)
            else:
                dictionary[character] = 1
                lst.append(character)
        except ValueError:
            pass
    print(lst[0])

printFirstNonRepeatedCharacter("yyrryet")