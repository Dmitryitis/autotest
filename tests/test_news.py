import pytest
import testit
from pages.news import NewsPage

class TestNewsPage:
    @testit.workItemIds([55])
    @testit.displayName('test_search_news')
    def test_search_news(self, browser):
        news = NewsPage(browser)
        news.check_search_news()

    @testit.workItemIds([56])
    @testit.displayName('test_sort_by_tabs')
    def test_sort_by_tabs(self, browser):
        news = NewsPage(browser)
        news.check_sort_tabs()