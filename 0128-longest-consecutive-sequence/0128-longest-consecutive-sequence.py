class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest_sequence = 0

        for num in numSet:
            if num-1 not in numSet:
                current_num = num
                current_sequence = 1
               
                while (current_num+1) in numSet:
                    current_num+=1
                    current_sequence+=1

                longest_sequence = max(longest_sequence, current_sequence)

        return longest_sequence




        