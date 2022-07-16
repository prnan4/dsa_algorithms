class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        def construct_dict(string):
            output_dict = {}
            for ch in string:
                if ch in output_dict:
                    output_dict[ch] += 1
                else:
                    output_dict[ch] = 1
            return output_dict
        
        magazine_dict = construct_dict(magazine)
        ransomeNote_dict = construct_dict(ransomNote)
        
        for ch in ransomeNote_dict:
            if ch not in magazine_dict:
                return False
            
            if ransomeNote_dict[ch] > magazine_dict[ch]:
                return False
            
        return True
        