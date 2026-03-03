class Solution(object):
    def canAliceWin(self, nums):
       total = sum(nums)
       single = sum(x for x in nums if x<10)
       double = total - single

       return single!=double