class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        w=0
        for i in range(k):
            w+=nums[i]
        sm=w
        for i in range(k,len(nums)):
            w=w-nums[i-k]+nums[i]
            sm=max(w,sm)  
        return sm/k 
        