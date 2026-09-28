class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = {}
        for element in s:
            if element in s_dict:
                s_dict[element] += 1
            else:
                s_dict[element] = 1
        for element in t:
            if element not in s_dict:
                return False
            else:
                s_dict[element] -= 1
                if s_dict[element] < 0:
                    return False
        return True