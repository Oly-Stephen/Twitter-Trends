from Sentiments import SentimentWords
from comp_sent import CompareSentiments
from tweets_info import Tweet, extract_tweets

if __name__ == '__main__':
    # Define file paths
    tweet_file_path = 'test_case/weekend_tweets2014.txt'
    sentiment_file_path = 'sentiments.csv'

    # Extract tweets
    tweets = extract_tweets(tweet_file_path)

    # Process sentiment words
    sentiment_words = SentimentWords(sentiment_file_path)
    sentiment_word_scores = sentiment_words.process_file()

    # Analyze tweet sentiment
    sentiment_analyzer = CompareSentiments(sentiment_word_scores)
    total_sentiment_score = 0
    for tweet in tweets:
        sentiment_score = sentiment_analyzer.compare_tweet_sentiment(tweet)
        total_sentiment_score += sentiment_score

    print("Total sentiment score:", total_sentiment_score)




