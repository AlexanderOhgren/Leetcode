class Solution(object):
    def maxProfit(self, prices):
        left_pointer, right_pointer = 0, 1
        max_profit = 0

        while right_pointer < len(prices):
            if prices[right_pointer] > prices[left_pointer]:
                profit = prices[right_pointer] - prices[left_pointer]
                max_profit = max(max_profit, profit)
            else:
                left_pointer = right_pointer
            right_pointer += 1
        
        return max_profit