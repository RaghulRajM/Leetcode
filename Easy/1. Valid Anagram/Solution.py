#Approach1: Looking at the problem, the easiest way would be to use Hashmaps with O(n). 
#We may generate two hashmaps and compare for exact match.

def valid_anagram(string1, string2):
  #1st check is if two have equal lengths otherwise, return False
  if len(string1)!=len(string2):
    return False

  #Create two dictionaries to store the counts for each character
  count1 = dict()
  count2 = dict()

  for i in range(len(string1)):
    count1[string1[i]] = 1 + count1.get(string1[i],0)
    count2[string2[i]] = 1 + count2.get(string2[i],0)
  for c in count1:
    if count1[c] != count2.get(c,0):
      return False

  return True

#Approach2: Creating a counter directly for both dictionaries and comparing them:

def valid_anagram(string1, string2):
  #1st check is if two have equal lengths otherwise, return False
  if len(string1)!=len(string2):
    return False
  if Counter(string1)!=Counter(string2):
    return False
  return True

#Approach3: Considering the sorted order for both dictionaries and comparing them:
#This can sometime take o(1) memory.

def valid_anagram(string1, string2):
  #1st check is if two have equal lengths otherwise, return False
  if len(string1)!=len(string2):
    return False
  if sorted(string1)!=sorted(string2):
    return False
  return True
