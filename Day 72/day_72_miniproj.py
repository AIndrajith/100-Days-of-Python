from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER analyzer
analyzer = SentimentIntensityAnalyzer()

# function using textBlob
def analyze_sentiment_textblob(text):
    sentiment = TextBlob(text).sentiment.polarity
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"
    
# function using VADER
def analyze_sentiment_vader(text):
    sentiment_score = analyzer.polarity_scores(text)["compound"]
    if sentiment_score >= 0.05:
        return "Positive"
    elif sentiment_score <= 0.05:
        return "Negative"
    else:
        return "Neutral"

# Main function for user interaction
def analyze_user_input():
    while True:
        text = input("Enter a sentence for sentiment analysis (or type 'exit' to quite): ")
        if text.lower(text) == 'exit':
            print("Exiting Sentiment Analyzer")
            break
        print(f"TextBlob Sentiment: {analyze_sentiment_textblob(text)}")
        print(f"VADER Sentiment: {analyze_sentiment_vader(text)}")

# Run the sentiment analyzer
analyze_user_input()