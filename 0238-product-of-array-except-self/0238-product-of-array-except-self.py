class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pre=[0]*len(nums)
        p=1
        for i in range(len(nums)):
            pre[i]=p
            p*=nums[i]
        suff=[0]*len(nums)
        s=1
        for i in range(len(nums)-1,-1,-1):
            suff[i]=s
            s*=nums[i]
        res=[1]*len(nums)
        for i in range(len(nums)):
            res[i]=pre[i]*suff[i]
        return res        