class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n = max(len(a), len(b))
        a = a.zfill(n)
        b = b.zfill(n)

        res = ''
        c = 0
        for i in range(n-1, -1, -1):
            subsum = int(a[i]) + int(b[i]) + c  
            if subsum == 3:
                res = '1' + res
                c = 1
            elif subsum == 2:
                res = '0' + res
                c = 1
            elif subsum == 1:
                res = '1' + res
                c = 0
            else:
                res = '0' + res
                c = 0
        if c == 1:
            res = '1' + res
        return res

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n = max(len(a), len(b))
        a = a.zfill(n)
        b = b.zfill(n)

        res = ''
        c = 0
        for i in range(n-1, -1, -1):
            if int(a[i]) == 1:
                c += 1
            if int(b[i]) == 1:
                c += 1

            res = str(c % 2) + res 
            c = c// 2

        if c % 2 == 1:
            res = '1' + res 
        return res

            

 