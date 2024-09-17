"""
You are given two strings word1 and word2. Merge the strings by adding letters in 
alternating order, starting with word1. If a string is longer than the other, append 
the additional letters onto the end of the merged string.

Return the merged string.
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) == 0 and len(word2) == 0:
            return ""
    
        if len(word1) > 0 and len(word2) == 0:
            return word1
        
        if len(word1) == 0 and len(word2) > 0:
            return word2
        
        if len(word1) > 0 and len(word2) > 0:
            return word1[0] + word2[0] + self.mergeAlternately(word1[1:], word2[1:])
