class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n=len(nums)
        # res=n*(n+1)//2
        # sum_of_num=sum(nums)

        # return res-sum_of_num
        res=0
        for i in range(len(nums)+1):
            res^=i
        for j in range(len(nums)):
            res^=nums[j]
        return res
        

