class Solution:

    def encode(self, strs: List[str]) -> str:
        indexes = []
        count = 0
        for word in strs:
            count += len(word)
            indexes.append(count)

        message = ""
        for i in range(len(indexes)):
            message += str(indexes[i])+'-'

        message += "£"

        for word in strs:
            message += word
        
        return message

    def decode(self, s: str) -> List[str]:
        strs = s.split("£")
        indexes, words = strs[0].split('-')[:-1], strs[1]
        
        result_list = []
        old_index = 0
        for index in indexes:
            result_list.append(words[old_index:int(index)])
            old_index = int(index)

        return result_list