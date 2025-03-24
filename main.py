import requests
from bs4 import BeautifulSoup

def extract_news(company_name):
    url = f'https://news.google.com/search?q={company_name}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = []
    
    for item in soup.find_all('article')[:10]:  # Limit to 10 articles
        title_element = item.find('h3')
        summary_element = item.find('p')
        
        # Check if title_element is found
        title = title_element.get_text() if title_element else 'No title available'
        
        # Check if summary_element is found
        summary = summary_element.get_text() if summary_element else 'No summary available'
        
        articles.append({'title': title, 'summary': summary})
    
    return articles



