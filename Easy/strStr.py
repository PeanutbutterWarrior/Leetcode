def substring_index(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        for start_index, first_char in enumerate(haystack):
            if first_char == needle[0]:
                if len(needle) > len(haystack[start_index:]):
                    return -1
                
                for expected_char, actual_char in zip(needle, haystack[start_index:]):
                    if expected_char != actual_char:
                        break
                else:
                    return start_index
        return -1
