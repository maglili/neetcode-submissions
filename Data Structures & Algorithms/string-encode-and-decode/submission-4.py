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
        ans = []
        mode = 0 # 0: get the length, 1: append the char
        str_len = 0
        temp_str = ''
        
        for char in s:
            if (mode == 0):
                if char.isdigit() == True:
                    temp_str += char
                elif char == '#':
                    str_len = int(temp_str)
                    temp_str = ''

                    if str_len > 0:
                        mode = 1
                    else:
                        ans.append(temp_str)

                else:
                    assert(0)
            else:
                temp_str += char
                str_len -= 1
                if str_len == 0:
                    mode = 0
                    ans.append(temp_str)
                    temp_str = ''
        return ans
                

