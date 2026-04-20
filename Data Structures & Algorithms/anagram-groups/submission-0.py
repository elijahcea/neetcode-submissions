class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            if key not in keys:
                keys[key] = []
            keys[key].append(s)
            
        return list(keys.values())
        

        