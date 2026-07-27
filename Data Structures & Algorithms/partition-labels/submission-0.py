class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        tbl = {}
        for i, char in enumerate(s):
            tbl[char] = i

        res = []
        sub_len = 0
        end = 0
        for i, char in enumerate(s):
            sub_len += 1
            end = max(end, tbl[char])
            if i == end:
                res.append(sub_len)
                sub_len = 0
                end = i + 1

        return res
