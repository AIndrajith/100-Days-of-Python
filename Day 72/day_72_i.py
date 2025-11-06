# Using Pre-trained NLP Modesls for sentiment Detection

# pip install textblob vaderSentiment

# Building Sentiment Analyzer using TextBlob and VADER

    # textblob provides a simple way o analyze sentiment 
    # using pre-trained lexicons.

# -*- coding: utf-8 -*-

from textblob import TextBlob

def analyze_sentiment_textblob(text):
    sentiment = TextBlob(text).sentiment.polarity
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"
    
# example
text = "I absolutely love python programming"
print(f"Sentiment: {analyze_sentiment_textblob(text)}")


# VADER => Valence Aware Dictionary and Sentiment Reasoner.
# sentiment it uses the E
# Reasoner is optimized for short text such as tweets, reviews or messages

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment_vader(text):
    sentiment_score = analyzer.polarity_scores(text)["compound"]
    if sentiment_score >= 0.05:
        return "Positive"
    elif sentiment_score <= 0.05:
        return "Negative"
    else:
        return "Neutral"
    
# Example
text = "This movie was amazing!"
print(f"Sentiment: {analyze_sentiment_vader(text)}")