import tweepy
from textblob import TextBlob

auth = tweepy.OAuthHandler("jsUkDhRj9GiozK9W7UsiFeOdU", "87MsAB65YfRAxcyiCMauqrcPJiBe6T6HuXJt4nlylod6MfchGk")
auth.set_access_token("1306553325949599745-edjMFM1U0ZLvXOljUTNy9bvbHMKxch", "LmU02Yik8JU3bkDAtTKblIAW5HBMn4sia3B72YJ5ZLC5O")

api = tweepy.API(auth)

public_tweets = api.search('Barack Obama')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    # Sentiment
    if analysis.sentiment.polarity < 0:
        print("Negative review")
    elif analysis.sentiment.polarity > 0:
        print("Positive review")
    else:
        print("Neutral review")



