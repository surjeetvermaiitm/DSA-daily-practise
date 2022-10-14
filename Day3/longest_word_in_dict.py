# Link: https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

class Solution(object):
    def check(self,sword,sdict):
        i=0
        j=0
        while i<len(sword) and j<len(sdict):
            if sword[i]==sdict[j]:
                j+=1
                i+=1
            else:
                i+=1
        return j==len(sdict)
                                
        
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """
        res=""
        for str_d in dictionary:     
            if self.check(s,str_d):
                if (len(res)<len(str_d) or ((len(res)==len(str_d)) and (res>str_d))):
                    res=str_d
        return res
                    
                
        
        
        