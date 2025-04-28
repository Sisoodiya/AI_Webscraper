import streamlit as st

# Toggle between local and remote scraping by changing the import below:
# For a local Chrome driver: use 'scraper'
# For Brightdata proxy service: use 'scrape'

from scrape import (
    scrape_website,
    split_dom_content,
    clean_body_content,
    extract_body_content
)
from parse import parse_with_ollama

st.title("AI Web Scraper")
url : str = st.text_input("Enter a Website URL : ")

if st.button("Scrape Site") :
    st.write(f"Scraping {url}...")

    result = scrape_website(url) # Scrape the website.
    body_content = extract_body_content(result) # Extract the body content.
    cleaned_content = clean_body_content(body_content) # Clean the body content.
    st.session_state.dom_content = cleaned_content # Store the cleaned content in the session state.
    # Session state is a dictionary that persists across reruns of the script.

    with st.expander("View DOM Content") : # Expander widget to hide the content by default.
        st.text_area("DOM Content", value = cleaned_content, height = 600) # Display the cleaned content.


if "dom_content" in st.session_state : # Check if the cleaned content is available in the session state.
    parse_description = st.text_area("Describe what you want to parse ?")

    if st.button("Parse Content") :
        if parse_description :
            st.write(f"Parsing content for '{parse_description}'...")
            dom_chunks = split_dom_content(st.session_state.dom_content) # Split the content into chunks.
            result = parse_with_ollama(dom_chunks, parse_description)
            st.write(result)