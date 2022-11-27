#Link: https://leetcode.com/problems/sort-characters-by-frequency/

class Solution:
    def frequencySort(self, s: str) -> str:
#         freq={ch:s.count(ch) for ch in s}
#         # def func(val):
#         #     return val[1]
#         print(freq.items())
#         sorted_dict=sorted(freq.items(),reverse=True,key=lambda x:x[1])
#         return "".join(x[0]*x[1] for x in sorted_dict)

        sorted_dict=Counter(s).most_common()
        print(sorted_dict)
        return "".join(x[0]*x[1] for x in sorted_dict)
        
        
        