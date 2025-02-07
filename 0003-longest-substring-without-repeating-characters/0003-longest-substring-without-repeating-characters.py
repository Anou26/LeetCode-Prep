class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = []
        max_len = 0

        for i in range(len(s)):
            res = []
            for j in range(i, len(s)):
                if s[j] in res:
                    break
                else:
                    res.append(s[j])
            max_len = max(max_len, len(res))
        return max_len