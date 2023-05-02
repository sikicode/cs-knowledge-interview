# Clarification
# 1. What to return when None repeats in array? not valid - don't consider
# 2. What to return when array is empty? not valid - don't consider
# 3. Any constraints on space and time?
# Pseudo-code
# use a dictionary to store key-value pairs, iterate through hash values to decide if there's a duplicate
# Optimize
# use a set to store values in nums, if value aready exists return True
# Implementation
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hset = set()
        for i in nums:
            if i in hset: return True
            else: hset.add(i)
        return False
# time complexity O(n) space O(n)
# Test cases