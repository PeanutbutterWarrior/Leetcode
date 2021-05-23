def maximum_sub_array(self, nums: List[int]) -> int:
    cumulative_sum = 0
    maximum = float('-inf')
    for item in nums:
        cumulative_sum += item
        if cumulative_sum < item:
            cumulative_sum = item
        if cumulative_sum > maximum:
            maximum = cumulative_sum
    return maximum
