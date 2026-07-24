class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        idle_time_to_trg = []
        for i in range(len(speed)):
            time_ = (target - position[i]) / speed[i]
            idle_time_to_trg.append((position[i], time_))
        idle_time_to_trg.sort()


        slow_car_time = None
        cnt = 0
        for pos, time in idle_time_to_trg[::-1]:
            if slow_car_time == None:
                slow_car_time = time
                cnt += 1
                continue
            if time > slow_car_time:
                cnt += 1
                slow_car_time = time
        return cnt