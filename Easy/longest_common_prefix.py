def longest_common_prefix(strs: List[str]) -> str:
    length = 0

    shortest = min(strs, key=len)
    max_length = len(shortest)

    while length < max_length:
        char = strs[0][length]
        for string in strs:
            if string[length] != char:
                return string[:length]
        length += 1

    return shortest