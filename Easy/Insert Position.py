def augmented_binary_search(self, nums: List[int], target: int) -> int:
    left_boundary = 0
    right_boundary = len(nums) - 1
    
    while True:
        midpoint = (left_boundary + right_boundary) // 2
        
        if left_boundary > right_boundary:
            return midpoint + 1
            
        if nums[midpoint] < target:
            left_boundary = midpoint + 1
        elif nums[midpoint] > target:
            right_boundary = midpoint - 1
        else:
            return midpoint
