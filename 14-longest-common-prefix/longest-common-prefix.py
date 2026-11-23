class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        minLen = min(len(s) for s in strs)
        prefix = ""
        
        if minLen == 0:
            return prefix
        
        for i in range(minLen):
            for word in strs:
                if len(prefix) == i:
                    prefix += word[i]
                elif prefix[i] != word[i]:
                    return prefix[:i]

        return prefix
            
        #Initialize a prefix
        #Iterate through strings, only add a letter if the ith element of every word is the same
        #If not, return prefix