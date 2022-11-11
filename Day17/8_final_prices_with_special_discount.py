#link: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        n=len(prices)
        st=[n-1]
        ans=[0]*n
        ans[n-1] = prices[n-1]
        for i in range(len(prices)-2,-1,-1):
            while st and prices[st[-1]]>prices[i]:
                st.pop()
            if st:
                ans[i]=prices[i]-prices[st[-1]]
            else:
                ans[i]=prices[i]
            st.append(i)
        return ans
                