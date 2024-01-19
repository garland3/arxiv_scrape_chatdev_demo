from flask import Flask, render_template
from scraper import ArxivScraper
app = Flask(__name__,template_folder=".")
@app.route('/')
def index():
    scraper = ArxivScraper()
    papers = scraper.get_recent_papers()
    return render_template('index.html', papers=papers)
@app.route('/scraper')
def scrape():
    scraper = ArxivScraper()
    scraper.scrape_arxiv()
    # return render_template('index.html', papers=papers)
    return "done"
if __name__ == '__main__':
    app.run()