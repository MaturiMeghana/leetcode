class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in range(len(nums)):
            if d.get(nums[i]):
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        maxi=0
        res=0
        for key,val in d.items():
            if val>maxi:
                maxi=val
                res=key
        return res        