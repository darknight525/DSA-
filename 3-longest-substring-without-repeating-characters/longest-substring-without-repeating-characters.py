class Solution(object):
    def lengthOfLongestSubstring(self, s):
        mp = {}
        left = 0
        ans = 0
        for right in range(len(s)):
            if s[right] in mp and mp[s[right]] >=left:
                left = mp[s[right]] + 1
            mp[s[right]] = right
            ans = max(ans,right - left + 1)
        
        return ans
            
            