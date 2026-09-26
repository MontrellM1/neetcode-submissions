class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {}
        
        for word in strs:
            key = tuple(sorted(word))
            if key not in d:
                d[key] = [word]
            else:
                d[key].append(word)
        return list(d.values())
        