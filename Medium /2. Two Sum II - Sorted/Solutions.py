#Approach 1. Using Hashmap like the old problem
def twoSum(numbers: List[int], target: int) -> List[int]:
  
  hashMap = dict()
  
  for i,j in enumerate(numbers):
    
      if target-j in hashMap:
          return ([hashMap[target-j],i+1])
        
      hashMap[j] = i+1

#Approach 2. Using start and end pointers. The array is sorted
#So, start with left most value and right most value
#Keep incrementing or decrementing based on the target comparison

def twoSum(numbers: List[int], target: int) -> List[int]:

  l, r = 0, len(numbers)-1
  
    while l < r:
        cumSum = numbers[l] + numbers[r]
      
        if cumSum == target:
            return ([l+1,r+1])
          
        elif cumSum < target:
            l += 1 #+1 because the indexes were returned +1 in the question
          
        else:
            r -= 1
    return None
