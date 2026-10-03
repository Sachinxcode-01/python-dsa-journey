class Solution:
    def plusOne(self, digits):
        # Traverse the array from right to left
        for i in range(len(digits) - 1, -1, -1):
            # If the current digit is less than 9, just add 1 and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the digit is 9, it becomes 0 and we carry over 1 to the next iteration
            digits[i] = 0
            
        # If all digits were 9, we need to add a 1 at the beginning
        return [1] + digits