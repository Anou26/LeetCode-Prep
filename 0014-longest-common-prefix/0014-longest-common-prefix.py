class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        strs.sort()
        first_str = strs[0]
        last_str = strs[-1]
        
        common_prefix = ''
        i = 0

        while i < len(first_str):
            if first_str[i] == last_str[i]:
                common_prefix += first_str[i]
            else:
                break
            i+=1

        return common_prefix

        