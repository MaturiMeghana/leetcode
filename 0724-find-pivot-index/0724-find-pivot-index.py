class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        s=0
        for i in range(len(nums)):
            s+=nums[i]
        for i in range(len(nums)):
            if (left==(s-left-nums[i])):
                return i
            left+=nums[i]
        return -1

       
