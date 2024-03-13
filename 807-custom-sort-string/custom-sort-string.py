class Solution:
    def customSortString(self, order: str, s: str) -> str:
        included_char = ""
        excluded_char = ""
        for c in s:
            if c not in order:
                excluded_char += c
        for c in order:
            if c in s:
                included_char += (c*s.count(c))
        return included_char + excluded_char