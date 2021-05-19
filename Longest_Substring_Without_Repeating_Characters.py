def lengthOfLongestSubstring(s: str) -> int:
    substr = ''
    p = longest = 0

    while p < len(s):
        if s[p] in substr:
            if len(substr) > longest:
                longest = len(substr)
            substr = substr[1:]
        else:
            substr += s[p]
            p += 1

    return max(longest, len(substr))
