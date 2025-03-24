import streamlit as st
from utils import extract_news, analyze_sentiment, comparative_analysis, text_to_speech 

st.title("News Sentiment Analysis")

company_name = st.text_input("Enter Company Name:")
if st.button("Fetch News"):
    if company_name:
        articles = extract_news(company_name)
        sentiment_results = analyze_sentiment(articles)
        sentiment_counts = comparative_analysis(sentiment_results)

        st.write("Sentiment Analysis Results:")
        for result in sentiment_results:
            st.write(f"**Title:** {result['title']}")
            st.write(f"**Summary:** {result['summary']}")
            st.write(f"**Sentiment:** {result['sentiment']}")
            st.write("---")

        st.write("Comparative Sentiment Analysis:")
        st.write(sentiment_counts)

        # Convert summarized content to speech
        if st.button("Convert to Speech"):
            combined_summary = " ".join([result['summary'] for result in sentiment_results])
            text_to_speech(combined_summary)
    else:
        st.warning("Please enter a company name.")
