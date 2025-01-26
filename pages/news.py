from data.assertions import Assertions
from pages.base import Base
from locators.NewsPage import NewsLocators

class NewsPage(Base):
    def __init__(self, page):
        super().__init__(page)
        self.assertions = Assertions(page)
    
    def check_search_news(self):
        self.open('news')

        self.assertions.check_URL('news', "Wrong URL")

        self.input(NewsLocators.INPUT_SEARCH, 'fdsfsdsgsgsgfgfs')
        self.click(NewsLocators.BUTTON_SEARCH)
        self.page.wait_for_timeout(2000)

        self.assertions.check_presence(NewsLocators.LOADER_404,'')
        
        self.click(NewsLocators.CLEAR_BUTTON_SEARCH)
        news_title = self.get_text(NewsLocators.NEWS_TITLE,0).strip()

        self.input(NewsLocators.INPUT_SEARCH, news_title)

        self.click_enter()

        self.assertions.check_equals(news_title, self.get_text(NewsLocators.NEWS_TITLE,0).strip(), '')

        self.click(NewsLocators.CLEAR_BUTTON_SEARCH)

    def check_sort_tabs(self):
        self.open('news')

        self.assertions.check_URL('news', "Wrong URL")