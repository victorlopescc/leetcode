list = ["flower","flow","flight"]

def longestCommonPrefix(strs):
    if not strs:
        return ""
    shortest = min(strs,key=len)
    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
    return shortest

print(longestCommonPrefix(list))