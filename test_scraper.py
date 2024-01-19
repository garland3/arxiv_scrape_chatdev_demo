import pytest
from scraper import ArxivScraper
@pytest.fixture
def scraper():
    return ArxivScraper()
def test_create_table(scraper):
    assert scraper.create_table() is None
def test_get_recent_papers(scraper):
    papers = scraper.get_recent_papers()
    assert isinstance(papers, list)
def test_scrape_arxiv(scraper):
    scraper.scrape_arxiv()
    papers = scraper.get_recent_papers()
    assert len(papers) > 0