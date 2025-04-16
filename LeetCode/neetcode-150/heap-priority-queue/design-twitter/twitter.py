class Twitter:

    def __init__(self):
        self.post_count = 0
        self.following = defaultdict(set)
        self.posts = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.post_count, tweetId))
        self.post_count += 1

        def getNewsFeed(self, userId: int) -> List[int]:
        news = []
        recent_posts = []
        max_heap = []
        if len(self.following[userId]) >= 9:
            for following in self.following[userId] | {userId,}:
                if following in self.posts:
                    index = len(self.posts[following]) - 1
                    post_count, tweet = self.posts[following][index]
                    heapq.heappush(max_heap, [-post_count, tweet, following, index - 1])
                    if len(max_heap) > 10:
                        heapq.heappop(max_heap)
            while max_heap:
                post_count, tweet, following, index = heapq.heappop(max_heap)
                heapq.heappush(recent_posts, [-post_count, tweet, following, index])
        else:
            for following in self.following[userId] | {userId,}:
                if following in self.posts:
                    index = len(self.posts[following]) - 1
                    post_count, tweet = self.posts[following][index]
                    heapq.heappush(recent_posts, [post_count, tweet, following, index - 1])

        while recent_posts and len(news) < 10:
            _, tweet, following, index = heapq.heappop(recent_posts)
            news.append(tweet)
            if index >= 0:
                post_count, tweet = self.posts[following][index]
                heapq.heappush(recent_posts, [post_count, tweet, following, index - 1])
        return news

    def getNewsFeed1(self, userId: int) -> List[int]:
        news = []
        recent_posts = []

        for following in self.following[userId] | {userId,}:
            if following in self.posts:
                index = len(self.posts[following]) - 1
                post_count, tweet = self.posts[following][index]
                heapq.heappush(recent_posts, [post_count, tweet, following, index - 1])

        while recent_posts and len(news) < 10:
            _, tweet, following, index = heapq.heappop(recent_posts)
            news.append(tweet)
            if index >= 0:
                post_count, tweet = self.posts[following][index]
                heapq.heappush(recent_posts, [post_count, tweet, following, index - 1])
        return news

    def getNewsFeed2(self, userId: int) -> List[int]:
        news = deque()
        recent_posts = [] #10 min_heap
        for following in self.following[userId] | {userId,}:
            for post_count, tweet in reversed(self.posts[following]):
                heapq.heappush(recent_posts, [post_count, tweet])
                if len(recent_posts) > 10:
                    if heapq.heappop(recent_posts)[0] == post_count:
                        break
        while recent_posts:
            _, tweet = heapq.heappop(recent_posts)
            news.appendleft(tweet)
        return list(news)

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
