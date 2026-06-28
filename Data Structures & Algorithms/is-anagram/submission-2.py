class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lib = {}
        for letter in s:
            lib[letter] = lib.get(letter, 0) + 1
        for letter in t:
            if letter not in lib:
                return False
            lib[letter] -= 1
            if lib[letter] == 0:
                del lib[letter]
        return len(lib) == 0