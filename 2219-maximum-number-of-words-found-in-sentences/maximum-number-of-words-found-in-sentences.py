class Solution(object):
    def mostWordsFound(self, sentences):
        max_words = 0
        for s in sentences:
            max_words = max(max_words , s.count(" ") + 1)
        
        return max_words