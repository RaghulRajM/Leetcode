# Without division, the best way is to compute prefix and suffix arrays and multiply them at the end. Since o(n) + o(n) + o(n) = o(n),
# use combination of for loops one after the other

def productExceptSelf(nums):
    n = len(nums)
    
    # Initialize two arrays to store prefix and suffix products
    prefix_products = [1] * n
    suffix_products = [1] * n
    
    result = [1] * n  # Initialize the result array
    
    # Calculate prefix products
    prefix_product = 1
    for i in range(n):
        prefix_products[i] = prefix_product
        prefix_product *= nums[i]
    
    # Calculate suffix products
    suffix_product = 1
    for i in range(n - 1, -1, -1):
        suffix_products[i] = suffix_product
        suffix_product *= nums[i]
    
    # Calculate the result using prefix and suffix products
    for i in range(n):
        result[i] = prefix_products[i] * suffix_products[i]
    
    return result

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

# Instead of having separate loops, we can compute on the fly!! Update prefix first and postfix while iterating over (len-i-1)

def productExceptSelf(self, nums: List[int]) -> List[int]:
    length=len(nums)
    sol=[1]*length
    pre = 1
    post = 1
    for i in range(length):
        sol[i] *= pre
        pre = pre*nums[i]
        sol[length-i-1] *= post
        post = post*nums[length-i-1]
    return(sol)
