class Solution(object):
    def subtractProductAndSum(self, n):
        temp = n
        sum = 0
        product = 1

        while temp>0:
            r = temp%10
            temp//=10
            sum+=r
            product*=r

        return product - sum

        
        