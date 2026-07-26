class Twitter:

    def __init__(self):
        self.follow_tbl = {} # key = userId, val = set of followeeId 
        self.post = {} # key = userId, val = list of post [(time, tweetId)]
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.post:
            self.post[userId] = []
        self.post[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.follow_tbl:
            self.follow_tbl[userId] = set([])
        self.follow_tbl[userId].add(userId)

        res = []
        for followeeId in self.follow_tbl[userId]:
            if followeeId not in self.post:
                continue
            for time, tweetId in self.post[followeeId]:
                res.append((time, tweetId))
        
        sorted_data = sorted(res, key=lambda x: x[0], reverse=True)
        return  [item[1] for item in sorted_data[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follow_tbl:
            self.follow_tbl[followerId] = set()
        self.follow_tbl[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follow_tbl:
            return
        self.follow_tbl[followerId].remove(followeeId)
