class Twitter:

    def __init__(self):
        # 使用 defaultdict，如果 key 不存在會自動建立空 set 或空 list
        self.follow_tbl = defaultdict(set)  # key = userId, val = set of followeeId 
        self.post = defaultdict(list) # key = userId, val = list of post [(time, tweetId)]
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # 數字越大代表時間越新
        self.post[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = [] # (time, tweetId, followeeId, idx)

        # 包含自己關注的人
        followees = set(self.follow_tbl[userId])
        followees.add(userId) # 確保包含自己
        
        for followeeId in followees:
            idx = len(self.post[followeeId]) - 1
            if idx >= 0:
                time, tweetId = self.post[followeeId][idx]
                heapq.heappush(min_heap, (time, tweetId, followeeId, idx - 1))

        while len(min_heap) and len(res) < 10:
            time, tweetId, followeeId, idx = heapq.heappop(min_heap)
            res.append(tweetId)
            if idx >= 0:
                time, tweetId = self.post[followeeId][idx]
                heapq.heappush(min_heap, (time, tweetId, followeeId, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follow_tbl[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            # discard 比 remove 安全，不存在時不會噴 Error
            self.follow_tbl[followerId].discard(followeeId)
