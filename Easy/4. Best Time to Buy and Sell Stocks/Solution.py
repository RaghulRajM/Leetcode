# Approach 1: Brute Force - Do it with two loops: Start on left side and go all the way to end
# by finding differences and return the max for i in range(len(prices)): for j in range(i+1, len(prices))..

#Approach 2: Sliding window
#We use a two pointer approach one to track min and other for max and a third variable to store max profit

def maxProfit(self, prices: List[int]) -> int:
  l = 0
  r = 1
  max_profit = 0
  
  while r < len(prices):
    if prices[r] > prices[l]:
      max_profit = max(max_profit, prices[r] - prices[l])
    else:
      l = r
    r += 1
    
  return (max_profit)

#This method works despite changing the pointer because we've a max variable that stores the history!!!
