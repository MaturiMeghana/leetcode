class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mini=min(nums)
        maxi=max(nums)
        while maxi!=0:
            mini,maxi=maxi,mini%maxi
        return mini 