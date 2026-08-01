class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=""
        val=""
        for ch in  s:
            if ch!=" ":
                res+=ch
        
            elif res:
                val=res+" "+val
                res=""
        if res:
            val=res+" "+val
            
        return val.strip()
        