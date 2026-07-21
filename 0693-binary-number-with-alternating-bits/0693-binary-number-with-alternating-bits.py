class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
      
        temp=-1
        while n>0:
            if n%2==temp:
                return False
            temp=n%2
            n=n//2
        return True
      

        