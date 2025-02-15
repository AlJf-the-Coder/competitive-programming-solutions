from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        pairs = []
        string = []
        def combination(lcount, rcount):
            if lcount < rcount or lcount > n:
                return
            if lcount == rcount == n:
                pairs.append("".join(string))
                return
            else:
                string.append("(")
                combination(lcount + 1, rcount)
                string.pop()
                string.append(")")
                combination(lcount, rcount + 1)
                string.pop()

        combination(0, 0)
        return pairs

class Solution1:
    def generateParenthesis(self, n: int) -> List[str]:
        num_iter = 2 ** (n * 2)
        comb = []
        for i in range(num_iter):
            stack = []
            parentheses = "".join(list(map(lambda x: "(" if x == "0" else ")", bin(i).removeprefix('0b').rjust(n*2, '0'))))
            valid = True
            for parenthesis in parentheses:
                if parenthesis == ")":
                    if stack == []:
                        valid = False
                        break
                    stack.pop()
                else:
                    stack.append(parenthesis)
            valid = False if not valid else stack == []
            if valid:
                comb.append(parentheses)
        return comb


