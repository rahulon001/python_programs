def string_contains_digits(string: str) -> bool:
    for s in string:
        if not (s.isdigit()):
            return False
        return True


print(string_contains_digits("1234"))
