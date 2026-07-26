class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        idle_time_to_trg = []
        for i in range(len(speed)):
            time_ = (target - position[i]) / speed[i]
            idle_time_to_trg.append((position[i], time_))
        idle_time_to_trg.sort()


        stack = []
        cnt = 0
        for pos, time in idle_time_to_trg[::-1]:
            print(pos, time)
            if stack and time <= stack[-1]:
                stack.pop()
                stack.append(time)
            else:
                stack.append(time)
                cnt += 1
        return cnt