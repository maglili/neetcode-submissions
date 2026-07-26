class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tbl = defaultdict(list) # [(bmp, index)]
        for idx, word in enumerate(strs):
            bmp = 0
            for char in word:
                bmp |= 1 << (ord(char) - ord('a'))
            tbl[bmp].append(idx)
        
        res = []
        for key,val in tbl.items():
            sub_res = []
            for idx in val:
                sub_res.append(strs[idx])
            res.append(sub_res)
        return res