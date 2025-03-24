def comparative_analysis(sentiment_results):
    sentiment_counts = {'Positive': 0, 'Negative': 0, 'Neutral': 0}
    
    for result in sentiment_results:
        sentiment_counts[result['sentiment']] += 1
    
    return sentiment_counts
