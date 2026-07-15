class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num>=10:
            total=0
            while num>0:
                    last=num%10
                    total+=last
                
                    num=num//10
            num=total
        return num
        

        