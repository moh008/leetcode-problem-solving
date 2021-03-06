from collections import defaultdict
class Solution:
    # Sol 1. Using a defaultdict
    def containsDuplicate(self, nums: List[int]) -> bool:
        m = defaultdict(int)
        for num in nums:
            if m[num]:
                return True
            m[num]+=1
        return False
    # Time Complexity: O(n)
    # Space Complexity: O(n), used a map, same memory as the array

    # Sol 2. Use a set externally
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        return len(nums)!=len(s)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
