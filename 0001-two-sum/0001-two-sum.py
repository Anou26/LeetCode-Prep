class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {} #holds a dictionary of indices
        
        for i, n in enumerate(nums): #i=index value of the current number, n=value of the current number
            diff = target - n
            if diff in numMap:
                return [numMap[diff], i]
            numMap[n] = i
            
        