class Solution:
    def addBinary(self, a, b):
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = []
        
        # Loop until both strings are exhausted and there is no carry left
        while i >= 0 or j >= 0 or carry:
            val = carry
            
            if i >= 0:
                val += int(a[i])
                i -= 1
            if j >= 0:
                val += int(b[j])
                j -= 1
            
            # Append the current bit (val % 2)
            res.append(str(val % 2))
            # Calculate the new carry (val // 2)
            carry = val // 2
            
        # The result is built backwards, so we reverse it and join into a string
        return ''.join(reversed(res))