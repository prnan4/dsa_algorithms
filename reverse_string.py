class Solution(object):
    # Time complexity O(n), space complexity O(n)
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        out = ""
        for i in range(len(s)-1, -1, -1):
            out += s[i]
        for i in range(0, len(s)):
            s[i] = out[i]

    # Iterative, two pointer approach
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            temp = s[left]
            s[left] =  s[right]
            s[right] = temp
            left += 1
            right -= 1
        