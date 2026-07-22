class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum=float('-inf')
        minimum=float('inf')
        for i in nums:
            if i>maximum:
                maximum=i
            if i<minimum :
                minimum=i
        while maximum!=0:
            minimum,maximum=maximum,minimum%maximum
        return minimum
        