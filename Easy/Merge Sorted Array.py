def merge_sorted_lists(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    index = 0
    for i in range(n):
        del nums1[-1]
    
    while nums2:
        if index >= len(nums1):
            nums1 += nums2
            break
        if nums1[index] < nums2[0]:
            index += 1
        else:
            nums1.insert(index, nums2.pop(0))
