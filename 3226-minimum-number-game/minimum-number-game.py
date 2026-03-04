class Solution(object):
    def numberGame(self, nums):
        nums.sort()
        result = []

        for i in range(0,len(nums),2):
            result.append(nums[i+1])
            result.append(nums[i])

        return result


       