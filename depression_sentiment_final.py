
import pandas as pd
from textblob import TextBlob

# Step 1: Simulated Social Media Posts
posts = [
    "I feel like nothing matters anymore.",
    "Life is beautiful and I'm grateful.",
    "Lately I’ve been so tired and hopeless.",
    "Just got promoted at work!",
    "I cry every night and I don’t know why.",
    "Excited to travel next week!",
    "I feel empty inside, even when I’m with people.",
    "So happy to see my friends again.",
    "It’s hard to get out of bed these days.",
    "Feeling energetic and ready to take on the day!",
    "Some days I just don't want to exist.",
    "I had a really productive and happy day.",
    "My heart feels heavy and I’m losing motivation.",
    "Enjoying the small things in life again.",
    "This sadness just won't go away.",
    "Looking forward to my birthday tomorrow!",
    "Why am I even trying anymore?",
    "Meditation has helped me feel balanced.",
    "I feel worthless and invisible.",
    "Had a peaceful walk with my dog."
]

# Step 2: Create DataFrame
df = pd.DataFrame(posts, columns=["Post"])

# Step 3: Sentiment Analysis
df["Polarity"] = df["Post"].apply(lambda x: TextBlob(x).sentiment.polarity)

# Step 4: Categorize Sentiment
def label_sentiment(p):
    if p < -0.3:
        return "Depressive"
    elif p > 0.3:
        return "Positive"
    else:
        return "Neutral"

df["Category"] = df["Polarity"].apply(label_sentiment)

# Step 5: Save to CSV
csv_file = "depression_sentiment_final.csv"
df.to_csv(csv_file, index=False)

# Step 6: Display Summary
summary = df["Category"].value_counts()
print("\nSentiment Distribution:")
print(summary)

print(f"\nData saved to {csv_file}")
