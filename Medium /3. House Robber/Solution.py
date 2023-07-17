#Approach 1 - Brute force 
  #For this list, [1,2,3,1] => we may go along different paths of a decision tree:
                     #/  \ 
                    #1    2
                  # / \    \
                  #3   1    1
  #We could go along each path and calculate the max

#Approach 2 - This is a classic example of a Dynamic Programming Problem!!

#We break down the bigger problem of decision trees and create sub problems
#Iterate for each item and have two temporary values stored which can give the
#max sum with and without considering the current item!!

def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        #[rob1, rob2, n, n+1,....]
        for i in nums:
            #If we consider rob1, then we look for the max_sum([ n, n+1,....])
            #Otherwise, max_sum([rob2, n, n+1,....])
            #This is more like a recursion
            temp = max(rob1 + i, rob2)
            rob1 = rob2
            rob2 = temp
        return (rob2)
