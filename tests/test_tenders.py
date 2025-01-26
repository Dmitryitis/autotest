import pytest
import testit
from pages.tenders import TendersPage

@pytest.mark.smoke
class TestTendersPage:
    @testit.workItemID(43)
    @testit.displayName('test_input_notice')
    def test_input_notice(self, browser):
        tender = TendersPage(browser)
        tender.check_input_notice()
