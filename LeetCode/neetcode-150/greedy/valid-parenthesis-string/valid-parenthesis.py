class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min = left_max = 0
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                left_min += 1
                left_max += 1
            elif c == ')':
                left_min -= 1
                left_max -= 1
                if left_max < 0:
                    return False
            else:
                left_min -= 1
                left_max += 1
            if left_min < 0:
                left_min = 0
        return left_min == 0

class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        stars = deque()
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                left.append(i)
            elif c == ')':
                if left:
                    left.pop()
                elif stars:
                    stars.popleft()
                else:
                    return False
            else:
                stars.append(i)

        for ind in left:
            while stars and stars[0] < ind:
                stars.popleft()
            if stars:
                stars.popleft()
            else:
                return False

        return True
