class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        count = 0
        for i in range(1,n):
            if n%i == 0:
                count+=1
                print(i)
                if count==k:
                    return i
        if count==k-1:
            return n
        return -1
            
        