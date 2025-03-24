import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from gtts import gTTS
import os

def extract_news(company_name):
    url = f'https://news.google.com/search?q={company_name}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = []
    
    for item in soup.find_all('article')[:10]:  # Limit to 10 articles
        title_element = item.find('h3')
        summary_element = item.find('p')
        
        title = title_element.get_text() if title_element else 'No title available'
        summary = summary_element.get_text() if summary_element else 'No summary available'
        
        articles.append({'title': title, 'summary': summary})
    
    return articles

def analyze_sentiment(articles):
    sentiment_results = []
    
    for article in articles:
        analysis = TextBlob(article['summary'])
        sentiment = analysis.sentiment.polarity
        
        if sentiment > 0:
            sentiment_label = 'Positive'
        elif sentiment < 0:
            sentiment_label = 'Negative'
        else:
            sentiment_label = 'Neutral'
        
        sentiment_results.append({
            'title': article['title'],
            'summary': article['summary'],
            'sentiment': sentiment_label
        })
    
    return sentiment_results

def comparative_analysis(sentiment_results):
    sentiment_counts = {'Positive': 0, 'Negative': 0, 'Neutral': 0}
    
    for result in sentiment_results:
        sentiment_counts[result['sentiment']] += 1
    
    return sentiment_counts

def text_to_speech(text, lang='hi'):
    tts = gTTS(text=text, lang=lang)
    tts.save('output.mp3')
    os.system('start output.mp3')  # Use 'open' for macOS
