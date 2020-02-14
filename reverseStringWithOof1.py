def reverseString(s) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    for i in range(len(s) // 2):
        k = s[len(s) - i - 1]
        s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
    print(s)


reverseString(["h", "e", "l", "l", "o"])
