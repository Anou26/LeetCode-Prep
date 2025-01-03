class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        vowels = set('aeiou')
        prefix_sum = [0]*n

#Count the number of strings that start and end with a vowel
        for i in range(n):
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix_sum[i] = 1
            if i>0:
                prefix_sum[i] += prefix_sum[i-1]

        ans = []

        for query in queries:
            count = prefix_sum[query[1]]
            if query[0] > 0:
                count -= prefix_sum[query[0] -1]
            ans.append(count)

        return ans







         