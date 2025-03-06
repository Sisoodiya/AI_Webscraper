import streamlit as st

st.title("AI Web Scraper")
url : str = st.text_input("Enter a Website URL : ")

if st.button("Scrape Site") :
    st.write(f"Scraping {url}...")