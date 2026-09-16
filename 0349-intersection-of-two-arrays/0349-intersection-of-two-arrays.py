class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res=set()
        nums2=set(nums2)
        for i in nums1:
            if i in nums2:
               res.add(i)
        return list(res)
        
            
