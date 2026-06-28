class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lib = {}
        key = (0,)*26
        for word in strs:
            temp_key = list(key)
            for letter in word:
                temp_key[ord(letter) - ord('a') + 1 ] += 1
            temp_key = tuple(temp_key)
            if temp_key not in lib:
                lib[temp_key] = [word]
            else:
                lib[temp_key].append(word)
        return list(lib.values())