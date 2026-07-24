class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_tbl = {}
        ans = []
        for str_ in strs:
            char_freq = [ 0 for i in range(26)] # 26 means 26 char
            for char in str_:
                char_freq[(ord(char) - 97)] += 1 # 97: a start from 97

            key = tuple(char_freq)
            
            if key not in hash_tbl:
                hash_tbl[key] = [str_]
            else:
                hash_tbl[key].append(str_)
        
        for _, val in hash_tbl.items():
            ans.append(val)
        
        return ans
