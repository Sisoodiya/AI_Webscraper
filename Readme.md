# AI Web Scraper

## Overview
This project demonstrates how to build an AI-powered web scraper using Python. The scraper is capable of extracting content from any website, processing the data with AI, and presenting the desired information in an organized format. The application uses web scraping techniques along with AI-based natural language processing to parse and extract relevant details from websites.

## Features
- **User-friendly Interface:** Built using Streamlit for an easy-to-use web UI.
- **Web Scraping Capabilities:** Utilizes Selenium and BeautifulSoup for data extraction.
- **AI Processing:** Uses LangChain with Llama 3 or other LLMs to parse and analyze scraped data.
- **Scalable and Robust:** Handles CAPTCHA challenges, IP bans, and large-scale data extraction using Bright Data.
- **Custom Queries:** Users can input prompts to extract specific information from a webpage.

## Technology Stack
- **Frontend:** Streamlit (for building the UI)
- **Web Scraping:** Selenium, BeautifulSoup
- **AI Integration:** LangChain, Llama 3 (or OpenAI API as an alternative)
- **Proxy and CAPTCHA Handling:** Bright Data
- **Virtual Environment Management:** Python venv

## Installation

### Prerequisites
Ensure you have Python installed (preferably 3.x) along with the necessary libraries.

### Setup
1. **Clone the repository**
   ```sh
   git clone https://github.com/sisoodiya/ai-web-scraper.git
   cd ai-web-scraper
   ```
2. **Create and activate a virtual environment**
   ```sh
   python3 -m venv ai-scraper-env
   source ai-scraper-env/bin/activate  # macOS/Linux
   ai-scraper-env\Scripts\activate     # Windows
   ```
3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Running the Application
1. Start the Streamlit UI:
   ```sh
   streamlit run main.py
   ```
2. Enter the website URL you want to scrape.
3. Provide a prompt describing the information you need.
4. Click on **Scrape Site** to fetch the content.
5. Click on **Parse Content** to process the scraped data with AI.

## Project Breakdown

### 1. Building the UI with Streamlit
- A simple input field for the website URL.
- A button to initiate scraping.
- A text area for user prompts.
- A section to display AI-processed data.

### 2. Web Scraping with Selenium
- Automates a browser to fetch webpage content.
- Uses a Chrome WebDriver to navigate websites.
- Extracts the page source (HTML).

### 3. Data Cleaning with BeautifulSoup
- Filters out unnecessary elements like `<script>` and `<style>`.
- Extracts meaningful text data for AI processing.

### 4. AI Processing with LangChain & Llama 3
- Uses an LLM to analyze and structure the extracted data.
- Accepts user prompts to determine what information to extract.
- Supports batch processing to handle large webpages.

### 5. Handling CAPTCHA and IP Bans with Bright Data
- Uses a proxy network to avoid being blocked.
- Solves CAPTCHA automatically for seamless scraping.

## Example Use Cases
- **E-commerce:** Extract product details, prices, and ratings.
- **Real Estate:** Collect property listings and price trends.
- **News Aggregation:** Gather headlines and summaries from multiple sources.
- **Research & Data Mining:** Scrape academic papers or structured data from websites.

## Future Improvements
- Implement asynchronous requests for faster scraping.
- Add support for more AI models (GPT-4, Claude, Gemini, etc.).
- Store and visualize extracted data in a database.
- Implement authentication for restricted websites.

## License
This project is licensed under the MIT License.

## Author
[Abhay Singh Sisoodiya](https://github.com/sisoodiya)

## Contributing
Feel free to open an issue or submit a pull request to improve this project!

Note : This project utilizes the chromedriver of version 13
```