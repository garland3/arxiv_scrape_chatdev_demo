import sqlite3
import requests
from datetime import date
from bs4 import BeautifulSoup
class ArxivScraper:
    def __init__(self):
        self.db_connection = sqlite3.connect('papers.db')
        self.create_table()
    def create_table(self):
        cursor = self.db_connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS papers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                date TEXT,
                title TEXT
            )
        ''')
        self.db_connection.commit()
    def get_recent_papers(self):
        cursor = self.db_connection.cursor()
        cursor.execute('SELECT name, date, title FROM papers ORDER BY date DESC')
        return cursor.fetchall()
    def scrape_arxiv(self):
        url = 'https://arxiv.org/list/cs.AI/recent'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        papers = soup.find_all('div', class_='list-title')
        today = date.today().strftime('%Y-%m-%d')
        cursor = self.db_connection.cursor()
        for paper in papers:
            print(f"{paper} ")
            # print(f"Scraping {paper.find('a').text.strip()}")
            # name = paper.find('a').text.strip()
            name = ""
            # title_div = paper.find('div', class_='list-title mathjax')
            # if title_div:
            #     full_text = title_div.text.strip()
            #     title_text = full_text.replace('Title:', '').strip()
            # else:
            #     print("No title found")
            #     title_text = ""
            descriptor_span = paper.find('span', class_='descriptor')
            if descriptor_span and descriptor_span.next_sibling:
                title_text = descriptor_span.next_sibling.strip()
                cursor.execute('INSERT INTO papers (name, date, title) VALUES (?, ?, ?)', (name, today, title_text))
            else:
                title_text = ""
                
            print(f"Scraping {title_text}")
            print("-----------------")
        self.db_connection.commit()
        
if __name__ == '__main__':
    scraper = ArxivScraper()
    scraper.scrape_arxiv()
    print(scraper.get_recent_papers())