import re


class Tweet:
    def __init__(self, location, datetime, text):
        self.location = location
        self.datetime = datetime
        self.text = text

    def get_words(self):
        # Remove non-word characters and split into words
        return re.findall(r'\w+', self.text)


def extract_tweets(file_path):
    tweets = []
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split('\t')
            location_parts = parts[0][1:-1].split(', ')
            try:
                location = [float(location_parts[0]), float(location_parts[1])]
            except ValueError:
                continue
            datetime = parts[2]
            text = parts[3]
            tweets.append(Tweet(location, datetime, text))
    return tweets
