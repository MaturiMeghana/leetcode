class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        ans=float('inf')
        curr_val=0
        for right in range(len(nums)):
            curr_val+=nums[right]
            while curr_val>=target:
                ans=min(ans,right-left+1)
                curr_val-=nums[left]
                left+=1
        if ans==float('inf'):
            return 0
        return ans
        
