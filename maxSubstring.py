"""longest substring without repeating characters"""

def lengthOfLongestSubstring(s):
    if len(s) == 0: return 0
    start = maxLength = 0
    usedChars = {}
    for i in range(len(s)):
        if s[i] in usedChars and start <= usedChars[s[i]]:
            start = usedChars[s[i]] + 1
        else:
            maxLength = max(maxLength, i - start + 1)
        usedChars[s[i]] = i
    return maxLength

print(lengthOfLongestSubstring("audfggeftydt"))