from typing import List
class Twitter:

    def __init__(self):
        self.user_id = dict()
        self.follower = dict()
        self.counter = 0
    def post_tweet(self, user_id, tweet_id):
        if user_id in self.user_id:
            self.user_id[user_id].append((tweet_id, self.counter))
            self.counter += 1
        else:
            self.user_id[user_id] = [(tweet_id, self.counter)]
            self.counter += 1
    def get_news_feed(self, user_id) -> List[int]:
        news_feed = []
        for news in self.follower[user_id]:
            news_feed += self.user_id[news]
        news_feed = sorted(news_feed, key = lambda x: x[1], reverse = True)
        return [item[0] for item in news_feed[:10]]

    def follow(self, follower_id, followee_id):
        if follower_id in self.follower:
            self.follower[follower_id].append(followee_id)
        else:
            self.follower[follower_id] = [followee_id]

    def unfollow(self, follower_id, followee_id):
        if follower_id in self.follower:
            self.follower[follower_id].remove(followee_id)
        else:
            print("No such user")


if __name__ == '__main__':
    twitter = Twitter()
    twitter.follow(1, 2)
    twitter.follow(1, 3)
    twitter.post_tweet(2, 4)
    twitter.post_tweet(2, 6)
    twitter.post_tweet(3, 2)
    twitter.post_tweet(3, 7)
    twitter.post_tweet(3, 3)
    twitter.post_tweet(3, 8)
    twitter.post_tweet(2, 1)
    twitter.post_tweet(2, 9)
    twitter.follow(1, 4)
    twitter.post_tweet(4, 5)
    twitter.post_tweet(4, 10)
    twitter.unfollow(1, 2)
    twitter.post_tweet(5, 11)
    twitter.post_tweet(5, 12)
    twitter.post_tweet(5, 13)
    twitter.post_tweet(6, 14)
    twitter.follow(1, 5)
    twitter.post_tweet(7, 15)
    twitter.post_tweet(7, 16)
    twitter.post_tweet(7, 17)
    twitter.post_tweet(7, 18)
    twitter.follow(1, 7)
    print(twitter.get_news_feed(1))

# code = []
# while date:= input():
#     code.append(date)
# code = '\n'.join(code)
# exec(code)