class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)    # Create a new list of length 2n
        for i in range(n):
            ans[i] = ans[i + n] = nums[i]  # Assign elements to ans
        return    
