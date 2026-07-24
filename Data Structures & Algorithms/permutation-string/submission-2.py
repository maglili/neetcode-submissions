class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # init table
        tbl1 = [0] * 26
        tbl2 = [0] * 26 
        for i in range(len(s1)):
            tbl1[ord(s1[i]) - ord('a') ] += 1
            tbl2[ord(s2[i]) - ord('a') ] += 1
        
        # calc match_cnt
        match_cnt = 0
        for i in range(26):
            if tbl1[i] == tbl2[i]:
                match_cnt += 1

        # scan the rest part of s2
        l = 0
        for r in range(len(s1), len(s2)):
            if match_cnt == 26:
                return True

            # update match_cnt
            index = ord(s2[r]) - ord('a')
            tbl2[index] += 1
            if tbl2[index] == tbl1[index]:
                match_cnt += 1
            elif tbl2[index] == tbl1[index] + 1:
                match_cnt -= 1

            index = ord(s2[l]) - ord('a')
            tbl2[index] -= 1
            if tbl2[index] == tbl1[index]:
                match_cnt += 1
            elif tbl2[index] == tbl1[index] - 1:
                match_cnt -= 1

            l += 1

        return match_cnt == 26