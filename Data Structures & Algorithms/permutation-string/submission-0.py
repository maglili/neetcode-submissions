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
        if match_cnt == 26:
            return True

        # scan the rest part of s2
        l = 0
        for r in range(len(s1), len(s2)):

            # update match_cnt
            if tbl2[ord(s2[r]) - ord('a')] + 1 == tbl1[ord(s2[r]) - ord('a') ]:
                match_cnt += 1
            elif tbl2[ord(s2[r]) - ord('a')] == tbl1[ord(s2[r]) - ord('a') ]:
                match_cnt -= 1

            if tbl2[ord(s2[l]) - ord('a')] - 1 == tbl1[ord(s2[l]) - ord('a') ]:
                match_cnt += 1
            elif tbl2[ord(s2[l]) - ord('a')] == tbl1[ord(s2[l]) - ord('a') ]:
                match_cnt -= 1

            # add new char and remove the most left one in tbl2
            tbl2[ord(s2[r]) - ord('a') ] += 1
            tbl2[ord(s2[l]) - ord('a') ] -= 1
            l += 1

            if match_cnt == 26:
                return True

        return False