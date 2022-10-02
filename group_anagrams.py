class Solution(object):
    # ========================== APPROACH 1 ==========================
    # Using mapping
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mapping = {}
        primes = [2, 3, 5, 7, 11 ,13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 107]
        
        for word in strs: 
            encoded = [0] * 26
            
            map_key = 1
            for ch in word: 
                index = ord(ch) - 97
                map_key *= primes[index]
            
            if map_key not in mapping:
                mapping[map_key] = [word]
            else:
                word_list = mapping[map_key]
                word_list.append(word)
                
                mapping[map_key] = word_list
        
        result = []
        for key in mapping:
            result.append(mapping[key])
            
        return result