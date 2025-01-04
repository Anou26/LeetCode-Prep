# input: nums -> List[int], val -> int
# nums = [4, 3, 5, 1], val = 5
# output: ans: int

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count +=1
            
        return count


        