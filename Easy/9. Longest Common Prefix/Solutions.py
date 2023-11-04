def longestCommonPrefix(self, strs: List[str]) -> str:
    sorted_str = sorted(strs)
    res = ""
    first = sorted_str[0]
    last = sorted_str[-1]
    for i in range(min(len(first),len(last))):
        if first[i]!=last[i]:
            return res
        else:
            res += first[i]
    return res
