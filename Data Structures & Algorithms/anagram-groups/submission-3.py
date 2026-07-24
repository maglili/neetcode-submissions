class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list) # key = cnt, val = list of word
        for word in strs:
            bmp = [0] * 26
            for char in word:
                bmp[ord(char) - ord('a')] += 1
            seen[tuple(bmp)].append(word)
        
        return list(seen.values())