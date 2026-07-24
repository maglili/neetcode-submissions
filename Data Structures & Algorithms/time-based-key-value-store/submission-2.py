class TimeMap:

    def __init__(self):
        # key: str
        # val: arr of (time, val)
        self.hash = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash:
            self.hash[key] = [(timestamp, value)]
        else:
            self.hash[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
            if key not in self.hash:
                return ""

            target_arr = self.hash[key]
            l = 0
            r = len(target_arr) - 1
            res = ""
            while l <= r:
                m = (l + r) // 2
                t, v = target_arr[m]

                if t == timestamp:
                    return v
                elif t > timestamp:
                    r = m - 1
                else:
                    l = m + 1
                    res = v

            return res
