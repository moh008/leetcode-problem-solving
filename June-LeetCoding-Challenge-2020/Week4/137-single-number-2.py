class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a, b = 0, 0 
        for i in nums:
            b = b ^ (a & i)
            a = a ^ i
            not_three = ~(a & b)
            a, b = not_three&a, not_three&b
        #print(a)
        #print(b)
        return a
    # O(N)
    # O(1)