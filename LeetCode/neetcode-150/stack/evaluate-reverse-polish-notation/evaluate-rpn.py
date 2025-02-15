class Solution(object):
    def evalRPN(self, tokens: list) -> int:
        stack = []
        for token in tokens:
            match token:
                case "/":
                    b = stack.pop()
                    a = stack.pop()
                    quotient = abs(a) // abs(b)
                    if a > 0 and b < 0 or a < 0 and b > 0:
                        quotient *= -1
                    stack.append(quotient)
                case "*":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a * b)
                case "+":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a + b)
                case "-":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a - b)
                case _:
                    stack.append(int(token))
        return stack[-1]

