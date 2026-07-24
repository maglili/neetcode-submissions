class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list) # key = cnt, val = list of index
        for idx, word in enumerate(strs):
            bmp = [0] * 26
            for char in word:
                bmp[ord(char) - ord('a')] += 1
            seen[tuple(bmp)].append(idx)
        
        res = []
        for idx in seen.values():
            cur = []
            for i in idx:
                cur.append(strs[i])
            res.append(cur)
        return res