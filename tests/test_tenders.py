import pytest
import testit
from pages.tenders import TendersPage

class TestTendersPage:
    @testit.workItemIds([43])
    @testit.displayName('test_input_notice')
    def test_input_notice(self, browser):
        tender = TendersPage(browser)
        tender.check_input_notice()
    
    @testit.workItemIds([46])
    @testit.displayName('test_check_filter_region')
    def test_check_filter_region(self, browser):
        tender = TendersPage(browser)
        tender.check_filter_by_region()
