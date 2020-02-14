def find_vowels_consonants_in_strings(string: str) -> None:
    string = string.lower()
    counter, counter1 = 0, 0
    for s in string:
        if ord(s) in [97, 101, 105, 111, 117]:
            counter += 1
        elif ord(s) in [x for x in [x for x in range(97, 122)] if x not in [97, 101, 105, 111, 117]]:
            counter1 += 1
    print("number of vowels in string are", counter)
    print("number of consonants in string are", counter1)


find_vowels_consonants_in_strings("number of vowels in string are")