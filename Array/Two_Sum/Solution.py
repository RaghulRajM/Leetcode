#Brute force - For the first element, check all other elements if they add up to target and similarly for all elements - O(n^2)
#Approach1: So again, we could implement this using a hashmap. Value would be the key and Index would be the value!!

def two_sum(nums, target):
  value_index_hash_map = dict()
  for i,j in enumerate(nums):
    if target-j in value_index_hash_map.keys():
        return ([value_index_hash_map[target-j], i])
    else:
        value_index_hash_map[j] = i
  return #This is redundant because the question says there is always a pair that adds up to the target

#Approach1: List index 

def two_sum(nums, target):
  for i,j in enumerate(nums):
    #if i!=len(nums)-1 -> This condition is not necessary because it's guaranteed to find a solution (we won't reach here)
    if target-j in nums[i+1:]:
      return(i,nums.index(target-j,i+1)) 
#Here we've i+1 because we want the index searching to start from next index (otherise when we've same numbers, It'll be a problem)
