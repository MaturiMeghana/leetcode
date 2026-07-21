class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        sumodd=n*n
        sumeven=n*(n+1)
        while sumeven!=0:
            sumodd,sumeven=sumeven,sumodd%sumeven
        return sumodd
        

        