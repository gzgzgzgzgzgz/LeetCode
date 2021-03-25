class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        result = []
        for word in dictionary:
            s_pointer = 0
            d_pointer = 0
            new_str = ""
            while s_pointer != len(s) and d_pointer != len(word):
                if s[s_pointer] == word[d_pointer]:
                    new_str += s[s_pointer]
                    d_pointer+=1
                s_pointer += 1
            if new_str == word:
                result.append(new_str)
        if result == []: return ""
        return sorted(sorted(result), key = lambda a: len(a), reverse = True)[0]   