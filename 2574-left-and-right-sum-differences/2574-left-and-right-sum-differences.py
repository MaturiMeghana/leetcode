class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lis=[]
        left=0
        s=0
        for i in range(len(nums)):
            s+=nums[i]
        for i in range(len(nums)):
            val=abs(left-(s-left-nums[i]))
            left+=nums[i]
            lis.append(val)
        return lis



        