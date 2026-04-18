class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        map1 = {}
        map2 = {}
        for string in s:
            count = map1.get(string)
            if not count:
                map1[string] = 1
            else:
                map1[string] = count + 1
        
        for string in t:
            count = map2.get(string)
            if not count:
                map2[string] = 1
            else:
                map2[string] = count + 1
        
        for key, val in map2.items():
            count = map1.get(key)
            if not count == val:
                return False
        
        return True
             

        