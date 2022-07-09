class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        def appendToOutput(num):
            if not output:

                output.append([])
                output.append([num])
            else:
                temp = output[:]
                for ele in temp:
                    if not ele:
                        print("k")
                        output.append([num])
                    else:
                        temp2 = ele[:]
                        temp2.append(num)
                        output.append(temp2)


        for num in nums:
            appendToOutput(num)
        
        return output


