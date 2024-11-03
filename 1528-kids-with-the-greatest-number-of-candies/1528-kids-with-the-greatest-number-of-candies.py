class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies = max(candies)
        return_list = []

        for candy in candies:
            return_list.append(candy + extraCandies >= max_candies)

        return return_list
