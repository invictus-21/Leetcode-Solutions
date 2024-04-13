class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count_subarrays(nums: List[int], bound: int) -> int:
            count = max_count = 0
            for num in nums:
                if num <= bound:
                    count += 1
                else:
                    count = 0
                max_count += count
            return max_count
        
        max_right = count_subarrays(nums, right)
        max_left = count_subarrays(nums, left - 1)
        
        return max_right - max_left
