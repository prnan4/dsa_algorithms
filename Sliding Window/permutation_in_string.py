class Solution:

    # Time limit exceeded
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # Generate all permutations of s1
        def generate_permutations(str1):
            if len(str1) == 1:
                return [str1]

            permutations = []

            for i in range(0, len(str1)):
                rem_str = str1[:i] + str1[i+1:]
                rem_str_permutations = generate_permutations(rem_str)

                for s in rem_str_permutations:
                    new_s = str1[i] + s
                    permutations.append(new_s)

            return permutations
        
        permutations_s1 = generate_permutations(s1)

        # Check for all permutations in string
        for s1 in permutations_s1:

            ptr_s1 = 0
            ptr_s2 = 0

            while (ptr_s1 != len(s1)) and (ptr_s2 != len(s2)):
                if s1[ptr_s1] == s2[ptr_s2]:
                    if s1 == s2[ptr_s2 : ptr_s2 + len(s1)]:
                        return True
                ptr_s2 += 1
        
        return False
    

    # Sort and check 
    def checkInclusion(self, s1: str, s2: str) -> bool:

        sorted_s1 = sorted(s1)
        for i in range(0, len(s2) - len(s1) + 1):
            sub_s2 = s2[i: i +  len(s1)]
            if sorted(sub_s2) == sorted_s1:
                return True
        return False