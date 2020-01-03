def reverseStr(s: str, k: int) -> str:
    if len(s) <= k:
        return s[::-1]
    if len(s) < 2*k:
        return s[:k][::-1]+s[k:]
    else:
        return s[:k][::-1]+s[k:2*k]+reverseStr(s[2*k:], k)




print(reverseStr("abcdefg", 2))