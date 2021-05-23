def add_one_to_list(self, digits: List[int]) -> List[int]:
    for index in range(len(digits) - 1, -1, -1):
        digits[index] += 1
        if digits[index] > 9:
            digits[index] = 0
        else:
            break
    else:
        digits.insert(0, 1)
    return digits
