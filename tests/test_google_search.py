import pytest
from pages.google_page import GooglePage
from utils.csv_reader import read_csv

data = read_csv("data/search_data.csv")

@pytest.mark.parametrize("test_data", data)
def test_google_search(page, test_data):
    google = GooglePage(page)
    search_term = test_data["search_term"]

    google.search(search_term)
    results = google.get_results()

    assert len(results) > 0
