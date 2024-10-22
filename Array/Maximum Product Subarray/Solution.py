# Using dynamic programming.. We track the max and min values instead of iterating O(n**2) times.

def maxProduct(self, nums: List[int]) -> int:
    res = max(nums)
    maxprod = 1
    minprod = 1
    for i in nums:
        if i == 0:
            maxprod = 1
            minprod = 1
            continue
        temp = maxprod
        maxprod = max(i, temp*i, minprod*i)
        minprod = min(i, temp*i, minprod*i)
        res = max(res, maxprod)
    return res
