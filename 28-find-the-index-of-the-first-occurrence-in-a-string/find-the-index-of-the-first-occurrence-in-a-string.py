class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        j = 0
        i = 0
        m = len(haystack)
        while i<(m-n+1):
            j=0
            while haystack[i+j] == needle[j]:
                j+=1
                if j==n:
                    return i
            i+=1
        return -1