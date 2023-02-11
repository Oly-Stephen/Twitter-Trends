

class CompareSentiments:
    def __init__(self, sentiment_words):
        self.sentiment_words = sentiment_words

    def compare_tweet_sentiment(self, tweet):
        sentiment_score = 0
        words = tweet.get_words()
        for word in words:
            if word in self.sentiment_words:
                sentiment_score += self.sentiment_words[word]

        return sentiment_score
