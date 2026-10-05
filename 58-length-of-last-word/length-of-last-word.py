class Solution(object):

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        i = len(s) - 1

        # Skip spaces at the end
        while i >= 0 and s[i] == ' ':
            i -= 1

        count = 0

        # Count the last word
        while i >= 0 and s[i] != ' ':
            count += 1
            i -= 1

        return count