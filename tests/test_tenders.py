import pytest
import testit
from pages.tenders import TendersPage

class TestTendersPage:
    @testit.workItemIds([43])
    @testit.displayName('test_input_notice')
    def test_input_notice(self, browser):
        tender = TendersPage(browser)
        tender.check_input_notice()
