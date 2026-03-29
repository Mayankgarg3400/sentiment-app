# import streamlit as st
# from textblob import TextBlob

# st.title("😊 Sentiment Analyzer AI")

# text = st.text_input("Enter your sentence:")

# if st.button("Analyze"):
#     if text:
#         analysis = TextBlob(text)
        

#         if analysis.sentiment.polarity > 0:
#             st.success("Positive 😊")
#         elif analysis.sentiment.polarity == 0:
#             st.info("Neutral 😐")
#         else:
#             st.error("Negative 😡")
#     else:
#         st.warning("Please enter some text")
# upgraded:
import streamlit as st
from textblob import TextBlob

# Page config
st.set_page_config(page_title="Sentiment Analyzer", page_icon="😊")

# Title
st.title("💬 Sentiment Analyzer AI")
st.markdown("Analyze the emotion of your text instantly 🚀")

# Input box
text = st.text_area("✍️ Enter your sentence:")

# Button
if st.button("🔍 Analyze"):
    if text.strip() == "":
        st.warning("⚠️ Please enter some text")
    else:
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity

        st.subheader("📊 Result:")

        # Score show
        st.write(f"Polarity Score: **{polarity:.2f}**")

        # Result logic
        if polarity > 0:
            st.success("😊 Positive Sentiment")
        elif polarity == 0:
            st.info("😐 Neutral Sentiment")
        else:
            st.error("😡 Negative Sentiment")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Mayank")
