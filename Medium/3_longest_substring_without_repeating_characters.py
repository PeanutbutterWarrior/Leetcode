class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        for start in range(len(s)):
            seen = set()
            for end in range(start, len(s) + 1):
                if end == len(s) or s[end] in seen:
                    break
                seen.add(s[end])
            if end - start > length:
                length = end - start
        return length