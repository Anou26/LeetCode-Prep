class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []

        for num in nums:
            if nums.count(num) > (n/3) and num not in result:
                result.append(num)

        return result