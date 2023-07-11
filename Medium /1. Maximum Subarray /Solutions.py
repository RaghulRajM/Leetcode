def maxSubArray(a: List[int]) -> int:
  maxSum = a[0]
  cumSum = 0
  for i in a:
    if cumSum < 0:
      cumSum = 0

    cumSum += i
    #Instead, we could do, max(maxSum, cumSum) but that's slow 
    if maxSum < cumSum:
      maxSum = cumSum
  return (maxSum)
#Because of function call overhead and irrespective of the condition 
#maxSum < cumSum being true or not, the function call will happen!!
