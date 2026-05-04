class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            freq = [0] * 26
            for letter in word:
                freq[ord(letter) - 97] += 1
            freq_str = " ".join(str(item) for item in freq)
            if freq_str in anagrams:
                print("Old word", freq_str)
                anagrams[freq_str].append(word)
            else:
                print("New word", freq_str)
                anagrams[freq_str] = [word]


        return list(anagrams.values())