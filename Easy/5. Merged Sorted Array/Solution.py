# Here, we'll iterate from the last of the list num1 (Comparing the greatest b/w 2 lists. 
  # Since it's given that list1 has space to accomodate all elements of list1 and list2 (with appended zeros). 
  # We don't have to worry about creating a new list!!!

def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_p = m - 1
        nums2_p = n - 1
        i = m + n - 1
        while nums1_p >= 0 and nums2_p >= 0:
            if nums1[nums1_p] > nums2[nums2_p]:
                nums1[i] = nums1[nums1_p]
                nums1_p = nums1_p - 1
            else:
                nums1[i] = nums2[nums2_p]
                nums2_p = nums2_p - 1
            i -= 1
        if nums2_p >= 0:
            nums1[:nums2_p+1] = nums2[:nums2_p+1]

  # If we want to save memory, we may remove the intermediate variables nums1_p and nums2_p!!
