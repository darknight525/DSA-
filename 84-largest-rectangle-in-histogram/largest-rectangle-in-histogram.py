class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        maxarea = 0
        heights.append(0)

        for i in range (len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                if stack:
                    w = i - stack[-1] -1
                else:
                    w = i
                maxarea = max(maxarea,h*w)
            stack.append(i)
        
        return maxarea
