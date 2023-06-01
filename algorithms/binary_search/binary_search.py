# 3 conditions 写法: https://stackoverflow.com/questions/30928268/binary-search-condition
# Induction Proof: http://www.cs.cornell.edu/courses/cs211/2006sp/Lectures/L06-Induction/binary_search.html
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1