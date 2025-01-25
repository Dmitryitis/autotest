import pytest
from pages.tenders import TendersPage

@pytest.mark.smoke
class TestTendersPage:
    def test_input_notice(self, browser):
        tender = TendersPage(browser)
        tender.check_input_notice()
