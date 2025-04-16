class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i], c = (digits[i] + c) % 10, (digits[i] + c) // 10
            if c == 0:
                break
        if c == 1:
            digits.insert(0, 1)
        return digits
