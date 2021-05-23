def length_of_last_word(self, s: str) -> int:
    s = s.strip()
    if not s:
        return 0
    try:
        return s[::-1].index(' ')
    except ValueError:
        return len(s)
