from collections import Counter

def numJewelsInStones(J: str, S: str) -> int:
    s_counts = Counter(S)
    sum = 0
    for j_element in J:
        if s_counts[j_element]:
            sum += s_counts[j_element]
    return sum

print(numJewelsInStones("aA", "aAAbbbb"))