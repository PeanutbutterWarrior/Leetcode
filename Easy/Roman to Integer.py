def roman_to_integer(s: str) -> int:
    numerals = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    s = list(s)
    value = 0
    
    while s:
        next_char = s.pop(0)
        if s and next_char + s[0] in numerals:
            value += numerals[next_char + s.pop(0)]
        else:
            value += numerals[next_char]
    
    return value