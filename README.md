
# Depression Detection via Sentiment Analysis

This project performs sentiment analysis on simulated social media posts to detect potential signs of depression using Python and Power BI.

🧠 Project Objective

To analyze sentiment polarity in user posts and classify them into:

Depressive

Neutral

Positive

🧰 Tools & Technologies

Python (TextBlob for sentiment analysis)

Pandas for data processing

Power BI for visualization

Google Colab / Local environment for execution

🧪 Methodology

1. Data Simulation

A set of realistic social media-style posts were manually curated to simulate public mental health expressions.

2. Sentiment Analysis

Used TextBlob to calculate the polarity score of each post.

Applied thresholds to classify:

Polarity < -0.3 → Depressive

-0.3 ≤ Polarity ≤ 0.3 → Neutral

Polarity > 0.3 → Positive

3. Data Export

Processed data was saved to depression_sentiment_final.csv for use in Power BI.

4. Visualization

Created visuals:

Pie Chart: Distribution of categories

Bar Chart: Average polarity by sentiment

Table: Full post + polarity + category

📂 Files Included

File Name

Description

depression_sentiment_final.py

Main Python script

depression_sentiment_final.csv

Output CSV file with labeled data

Ai_Infrastructure_Visualisation_SentimentalAnalysis.pbix

Power BI dashboard file

📊 Results Summary

Clear identification of depressive sentiment from textual cues

Strong polarity separation between emotional states

Easy-to-interpret visuals created with Power BI

✅ Conclusion

This project shows how simple NLP tools like TextBlob can help identify emotional tones in public content. It’s a foundation for more advanced mental health analysis in real-world applications.

🔗 References

TextBlob Documentation

Power BI

Pandas Library


