class Twitter:

    def __init__(self):
        # 使用 defaultdict，如果 key 不存在會自動建立空 set 或空 list
        self.follow_tbl = defaultdict(set)  # key = userId, val = set of followeeId 
        self.post = defaultdict(list) # key = userId, val = list of post [(time, tweetId)]
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # 數字越大代表時間越新
        self.post[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        
        # 包含自己關注的人
        followees = set(self.follow_tbl[userId])
        followees.add(userId) # 確保包含自己
        
        for followeeId in followees:
            # 直接抓出該使用者所有的發文，塞進候選池
            for time, tweetId in self.post[followeeId]:
                res.append((time, tweetId))
        
        # 核心優化：由大到小排（reverse=True），並只取前 10 個
        sorted_data = sorted(res, key=lambda x: x[0], reverse=True)
        return [item[1] for item in sorted_data[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follow_tbl[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            # discard 比 remove 安全，不存在時不會噴 Error
            self.follow_tbl[followerId].discard(followeeId)
