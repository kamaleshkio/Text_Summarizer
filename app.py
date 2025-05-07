import streamlit as st
from src.textSummarizer.pipeline.prediction import PredictPipeline

st.set_page_config(page_title="Text Summarizer", layout="wide")

st.title("Text Summarizer using NLP")

# Input text area
text_input = st.text_area("Enter text to summarize", height=300)

# When button is clicked
if st.button("Generate Summary"):
    if text_input.strip() == "":
        st.warning(" Please enter some text.")
    else:
        try:
            # Predict using your pipeline
            pipeline = PredictPipeline()
            summary = pipeline.predict(text_input)

            st.subheader("Summary:")
            st.success(summary)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Optional: Add sidebar info
with st.sidebar:
    st.title("About")
    st.markdown("""
        This is a simple app built using Streamlit and your custom `PredictPipeline`.
        
        - Supports long text inputs
        - Uses transformer/NLP models for summarization
        - Built by **B. Kamalesh**
    """)