class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        longest_palindrome = ""
        
        # Odd case
        for i in range(len(s)):
            j = 0
            while (i - j >= 0) and (i + j <= len(s) - 1) and s[i-j] == s[i+j]:
                sub = s[i-j: i+j+1]
                if len(sub) > len(longest_palindrome):
                    longest_palindrome = sub   
                j += 1
        
        # Even case
        for i in range(len(s)-1):
            j = 0
            while (i - j >= 0) and (i + j + 1 <= len(s) - 1) and (s[i] == s[i+1]) and s[i-j] == s[i+j + 1]:
                sub = s[i-j: i+j+2]
                
                if len(sub) > len(longest_palindrome):
                    longest_palindrome = sub   
                j += 1
        
        return longest_palindrome
            