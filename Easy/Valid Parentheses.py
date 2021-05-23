def is_valid_brackets(s: str) -> bool:
    openers = {'(': 0, '{': 1, '[': 2}
    closers = {')': 0, '}': 1, ']': 2}

    opened_brackets = []

    for char in s:
        if char in openers:
            opened_brackets.append(char)
        else:
            if not opened_brackets:
                return False
            
            if openers[opened_brackets.pop(-1)] != closers[char]:
                return False
                    
    return not opened_brackets
