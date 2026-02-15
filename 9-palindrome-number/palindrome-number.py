class Solution(object):
    def isPalindrome(self, x):
       temp = x
       rev = 0

       while temp>0:
          r = temp%10
          temp//=10
          rev = rev*10+r
        
       return rev ==x