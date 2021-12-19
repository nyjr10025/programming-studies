from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = max(prices)
        min_price = prices[0]
        true_min = min(prices)
        max_profit = 0
        for price in prices:
            if price == min_price:
                continue
            profit = price - min_price
            # if price is higher than current min and profit is higher than current profit
            if profit > max_profit:
                max_profit = profit
            # if price is the highest price and we passed the min peak then no profit possible afterwards, return current profit
            if price == max_price and min_price == true_min:
                return max_profit
            # if price is same or lower than current min, assign new min
            if price < min_price:
                min_price = price
        return max_profit
                    
yes = Solution()
print(yes.maxProfit([7,1,5,3,6,4]))
print(yes.maxProfit([2,4,1]))
print(yes.maxProfit([2,1,2,1,0,1,2]))

