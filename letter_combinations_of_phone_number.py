class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        char_dict = {2: ['a', 'b', 'c'], 3:['d', 'e', 'f'], 4:['g', 'h', 'i'], 5:['j', 'k', 'l'], 6:['m', 'n', 'o'], 7:['p', 'q', 'r', 's'], 8:['t', 'u', 'v'], 9:['w', 'x', 'y', 'z']}
        while digits:
            ch = digits[0]
            print(digits, ch)
            characters = char_dict[int(ch)]

            if not result:
                result = characters
            else:
                new_result = []
                for ch_i in result:
                    for ch_j in characters:
                        new_result.append(ch_i+ ch_j)
                result = new_result
                print(result)
            digits = digits[1:]
        return result
                        
            
        