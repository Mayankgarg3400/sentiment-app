import streamlit as st
from textblob import TextBlob

st.title("😊 Sentiment Analyzer AI")

text = st.text_input("Enter your sentence:")

if st.button("Analyze"):
    if text:
        analysis = TextBlob(text)

        if analysis.sentiment.polarity > 0:
            st.success("Positive 😊")
        elif analysis.sentiment.polarity == 0:
            st.info("Neutral 😐")
        else:
            st.error("Negative 😡")
    else:
        st.warning("Please enter some text")