def letter_to_phone_digits(digits: str, top_level: bool = True) -> List[str]):
    if len(digits) == 0:
        if top_level:
            return []
        else:
            return ['']
    
    digit_to_letter = {'2': 'abc', '3': 'def', '4': 'ghi',
                       '5': 'jkl', '6': 'mno', '7': 'pqrs',
                       '8': 'tuv', '9':'wxyz'}
    output = []
    for combination in self.letterCombinations(digits[1:], False):
        for letter in digit_to_letter[digits[0]]:
            output.append(letter + combination)
    
    return output