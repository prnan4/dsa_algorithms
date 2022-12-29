class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = 0
        max_len = 0
        ch_map = {}
        for i, ch in enumerate(s):
            if ch in ch_map:
                st = max(st, ch_map[ch] + 1)
            ch_map[ch] = i
            len_str = i - st + 1
            max_len = max(max_len, len_str)
            print(max_len)
        return max_len