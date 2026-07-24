class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []

        i = 0
        while i < len(s):
            j = i
            while j < len(s):
                if s[j] == "#":
                    w_len = int(s[i:j])
                    res.append(s[j+1:j+1+w_len])
                    i = j+1+w_len
                    j = i
                    continue
                j+=1
            i+=1
        
        return res