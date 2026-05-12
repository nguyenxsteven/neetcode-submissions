class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #set the min price, infinite to make it easy
        min_price = float('inf')

        #profit to 0 aka best profit found so far
        max_profit =  0

        #start the loop one by one
        for new_price in prices:
            #If today's price is lower than our current cheapest, update the buy price
            if new_price < min_price:
                min_price = new_price
            # Otherwise, check if selling TODAY gives us a better profit than before
            # new_price - min_price = profit if we bought at the lowest and sell now
            elif new_price - min_price > max_profit:
                max_profit = new_price - min_price
        # Return the best profit we found (0 if prices only went down)
        return max_profit
            