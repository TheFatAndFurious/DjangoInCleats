import tweepy, time

bearer_token="AAAAAAAAAAAAAAAAAAAAAM1FyAEAAAAALAj1E2DzriaoMF7MfNMppzVPGQw%3DCH36Odh3QjSRe5bkx1h1RzRHqAVcsoITXuP6gAXpoEaPKyDZaN"

def get_user_id(name):
    client = tweepy.Client(bearer_token)
    user = client.get_user(username=name)
    return user.data.id

def get_tweets_from_user(user_id):
    client = tweepy.Client(bearer_token)
    response = client.get_users_tweets(user_id)
    if response:
        for tweet in response.data:
            print(tweet.id)
            print(tweet.text)


username = "StadeToulousain"
user_id = get_user_id(username)
if user_id:
    print(f"user id is {user_id}")
    time.sleep(2)
get_tweets_from_user(user_id)

