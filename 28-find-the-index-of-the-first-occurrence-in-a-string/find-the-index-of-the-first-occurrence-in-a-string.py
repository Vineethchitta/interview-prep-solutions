class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        j = 0
        i = 0
        m = len(haystack)
        while i<(m-n+1):
            while haystack[i+j] == needle[j]:
                j+=1
                if j==n:
                    return i+j-n
            else:
                j = 0
            i+=1
        return -1