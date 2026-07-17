class Solution(object):
    def distinctDifferenceArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        pre={}
        suff={}
        res=[]
        for i in nums:
            if i in suff:
                suff[i]+=1
            else:
                suff[i]=1
        for i in nums:
            if i in pre:
                pre[i]+=1
            else:
                pre[i]=1
            suff[i]-=1
            if suff[i]==0:
                del suff[i]
            res.append(len(pre)-len(suff))
        return res
            
        

        