class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack)<len(needle):
            return -1
        n=len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+n]==needle:
                return i
        return -1

