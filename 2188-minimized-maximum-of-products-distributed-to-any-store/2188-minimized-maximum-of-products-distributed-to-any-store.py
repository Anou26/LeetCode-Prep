"""
Given: 
n: number of speciality retail stores
m: number of product types
quantities[i]: number of products of the i(th) product type
x: max. number of products given to each store

Constraints:
A store can be given atmost one product type but the amount can vary
m == quantities.length
1<=m<=n<=10^5

"""

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def can_distribute(x):
            stores_needed = 0
            for quantity in quantities:
                stores_needed += (quantity + x - 1) // x 
            return stores_needed <= n

        low, high = 1, max(quantities)
        while low < high:
            mid = (low + high) // 2
            if can_distribute(mid):
                high = mid  
            else:
                low = mid + 1  
        return low