import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download("stopwords")
stemmer = PorterStemmer()
stop_words = set(stopwords.words("english"))

# load dataset
df = pd.read_csv("spam.csv", encoding="latin-1")[["v1", "v2"]]
df.columns = ["label", "message"]
df["label"] = df["label"].map({"ham":0, "spam":1})

def preprocess_text(text):
    text = re.sub(r"\W", " ", text)     # Remove special characters
    text = text.lower()                 # convert to lowercase
    words = text.split()
    words = [stemmer.stem(word) for word in words if word not in stop_words]        # remove stop words and stem words
    return " ".join(words)

df["cleaned_message"] = df["message"].apply(preprocess_text)

print(df.head())