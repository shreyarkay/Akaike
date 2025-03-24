from textblob import TextBlob

def analyze_sentiment(articles):
    for article in articles:
        analysis = TextBlob(article['summary'])
        sentiment = analysis.sentiment.polarity
        if sentiment > 0:
            article['sentiment'] = 'Positive'
        elif sentiment < 0:
            article['sentiment'] = 'Negative'
        else:
            article['sentiment'] = 'Neutral'
    return articles
