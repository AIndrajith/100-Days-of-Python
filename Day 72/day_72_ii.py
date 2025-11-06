# Adding user input for Real-Time Analysis

from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment_textblob(text):
    sentiment = TextBlob(text).sentiment.polarity
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"
    
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment_vader(text):
    sentiment_score = analyzer.polarity_scores(text)["compound"]
    if sentiment_score >= 0.05:
        return "Positive"
    elif sentiment_score <= 0.05:
        return "Negative"
    else:
        return "Neutral"
    
def analyze_user_input():
    text = input("Enter a sentence for sentiment analysis: ")
    print(f"TextBlob Sentiment: {analyze_sentiment_textblob(text)}")
    print(f"VADER Sentiment: {analyze_sentiment_vader(text)}")

analyze_user_input()