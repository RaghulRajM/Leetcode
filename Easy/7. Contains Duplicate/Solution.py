
# List takes a lot of time, set is relatively faster and memory is kinda decent

def containsDuplicate(self, nums: List[int]) -> bool:
    empty = set()
    for i in nums:
        if i in empty:
            return True
        empty.add(i)
    return False

# BUT HASH LOOKUPS ARE THE FASTEST - CONSTANT TIME => O(n). But more memory

def containsDuplicate(self, nums: List[int]) -> bool:
    empty = dict()
    for i in nums:
        if i in empty:
            return True
        empty[i] = 1
    return False
