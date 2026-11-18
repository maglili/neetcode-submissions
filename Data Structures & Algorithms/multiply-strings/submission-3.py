class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                tmp = int(num1[i]) * int(num2[j])

                res[i + j] += tmp
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10

        res = res[::-1]

        beg = 0
        for i in range(len(res)):
            if res[i] != 0:
                beg = i
                break

        res = res[beg:]
        return "".join(map(str, res))
