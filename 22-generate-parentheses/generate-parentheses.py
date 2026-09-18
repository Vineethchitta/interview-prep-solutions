class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = set()
        res.add("()")
        if n==1:
            return list(res)
        for i in range(1, n):
            temp = set()
            for element in res:
                for j in range(0, len(element)):
                    temp.add(element[0:j]+"()"+element[j:len(element)])
            res = temp
        return list(res)