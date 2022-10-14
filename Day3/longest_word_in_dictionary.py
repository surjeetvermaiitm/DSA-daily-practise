#Link: https://leetcode.com/problems/longest-word-in-dictionary/

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        best = prefix = ""
        for w in sorted(words):
            if w[:len(w) - 1] == prefix[:len(w) - 1]:
                prefix = w
                best = max([best, w], key=len)
        return best