# We may solve this using 4 different approaches!!

# Approach 1: Plain recursion - Break down each nth step which can be reached from n-1th or n-2th step
# Say we've n = 5
#            4
#           /  \
#         3      2
#        / \    |  \
#       2   1   1   0
#      / \
#     1   0
# At all the leaf nodes, when n= 0 or 1, we return 1!!
def climbStairs(self, n: int) -> int:
  if n==0 or n==1:
    return 1
  return climbstairs(n-1) + climbstairs(n-2)


#Approach 2: Memoization (Top Down) - Breaking down each number recursively and eventually sum up all the results!
# This is same as recursion but we'll store the values of already computed results to avoid redundant calculations.
def climbStairs(self, n: int) -> int:
  memo = {}
    
  def helper(steps):
      if steps == 0:
          return 1
      
      # Check if the result is already memoized
      if steps in memo:
          return memo[steps]
      
      # Recursively calculate the number of ways for each step
      memo[steps] = helper(steps - 1) + helper(steps - 2)
      return memo[steps]

  return helper(n)

#Approach 3: Tabulation (Bottom Up) - Instead of breaking down each number, computing for each and every subtree
# and work your way up!!
# We may store the values of already computed results to avoid redundant calculations
def climbStairs(self, n: int) -> int:
  if n==0 or n==1:
    return 1
    dp = [0] * (n+1) #n+1 because we start from 0th step!!
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

#Approach 4: Space Optimization: Instead of storing the entire DP table, we may track only the last two values
def climbStairs(self, n: int) -> int:  
  if n == 0 or n == 1:
      return 1
  prev, curr = 1, 1
  for i in range(2, n+1):
      temp = curr
      curr = prev + curr
      prev = temp
  return curr
