#Link: https://leetcode.com/problems/custom-sort-string/

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        def func(val):
            if val in order:
                return order.index(val)
            else:
                return 0
        # print(func("a"))
        sorted_list=sorted(s,key = func)
        return "".join(sorted_list)
        
     
        
        