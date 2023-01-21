class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        out = []
        c = []
        res = []

        def backtrack(c, s):
            print(c, s, out)
            if len(s) > ((4 - len(c))* 3):
                return 
            if len(c) == 4 and s == '':
                out.append(c[:])
                return
            if len(c) == 4 or s == '':
                return
            for i in range(1, 4):
                if i > 1 and s[0] == '0':
                    continue
                if i == 3 and int(s[0:3]) > 255:
                    continue
                c.append(s[0:i])
                backtrack(c, s[i: len(s)])
                c.pop()
        backtrack(c, s)
        
        for val in out: 
            ip = ''
            for i in val:
                ip += i
                ip += '.'
            ip = ip[:-1]
            if ip not in res:
                res.append(ip)
        return res