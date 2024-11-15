# My brute force solution
class Solution(object):
    def maxProfit(self, prices):
        record=[]
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                top=max(prices[j:]) if prices[i] < max(prices[j:]) else prices[i]
                try:
                    top_index= prices.index(top, i+1)
                except ValueError:
                    top_index=None
                if top_index is not None:
                    if i < prices.index(top, i+1):
                        record.append(top-prices[i])
                    else:
                        continue
            record.append(0)
        
        if all(i==0 for i in record):
            return 0
        else:
            return max(record)

#better optimization with AI
def maxProfit(self, prices):
    # Initialize minimum price to a large value and maximum profit to 0
    min_price = float('inf')
    max_profit = 0

    # Iterate over each price in the list
    for price in prices:
        # Update the minimum price if the current price is lower
        min_price = min(min_price, price)
        
        # Calculate profit by selling at the current price after buying at the min_price
        profit = price - min_price
        
        # Update max_profit if the current profit is greater
        max_profit = max(max_profit, profit)

    return max_profit


