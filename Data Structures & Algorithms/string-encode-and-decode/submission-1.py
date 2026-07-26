class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = ''
        for str_ in strs:
            str_len = len(str_)
            encoding += str(str_len) +'#'
            encoding += str_
        print(encoding)
        return encoding

    def decode(self, s: str) -> List[str]:
        str_num = ''
        str_len = 0
        mode = 0
        temp_str = ''
        ans = []
        for char in s:
            if (mode == 0):
                if char.isdigit() == True:
                    str_num += char
                elif char == '#':
                    mode = 1
                    str_len = int(str_num)
                    str_num = ''
                else:
                    assert(0)
            else:
                temp_str += char
                if (str_len>0):
                    str_len -= 1
                if str_len == 0:
                    mode = 0
                    ans.append(temp_str)
                    temp_str = ''
        return ans
                

