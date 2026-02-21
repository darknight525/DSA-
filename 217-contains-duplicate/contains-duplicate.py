class Solution:
    def containsDuplicate(self, nums):
        mp ={}

        for x in nums:
            if x in mp:
                return True
            mp[x] = 1
        return False
       