class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * (n+1)

        #Initialize and calculate prefix sum
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]

        #Initialize count of valid splits to 0 first
        count = 0

        #Calculate valid splits
        for i in range(n-1):
            if prefix_sum[i+1] >= prefix_sum[n] - prefix_sum[i+1]:
                count+=1
        
        return count
            


