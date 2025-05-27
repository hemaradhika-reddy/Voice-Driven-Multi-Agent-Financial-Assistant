# data_ingestion/web_scraper.py
import requests
from bs4 import BeautifulSoup

class ScrapingAgent:
    def scrape_earnings(self, company_url):
        try:
            response = requests.get(company_url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            earnings_section = soup.find('div', class_='earnings-report') or soup.find('div', id='earnings')
            return earnings_section.get_text(strip=True) if earnings_section else "No earnings data found"
        except Exception as e:
            return f"Error scraping {company_url}: {str(e)}"