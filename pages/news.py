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

        text_link_bisness = self.get_text(NewsLocators.NEWS_ANCHOR_LINK, 0).split()
        text_link_news = self.get_text(NewsLocators.NEWS_ANCHOR_LINK,1).split()

        self.click(NewsLocators.NEWS_TAB_MAIN)

        self.page.wait_for_timeout(2000)

        text_active_anchor = self.get_text(NewsLocators.NEWS_ANCHOR_LINK_ACTIVE, 0).split()
        text_media_badge = self.get_text(NewsLocators.NEWS_MEDIA_BADGE, 0).split()
        self.assertions.check_equals(text_link_bisness, text_active_anchor, '')
        self.assertions.check_equals(text_link_bisness, text_media_badge, '')

        self.click_element_by_index(NewsLocators.NEWS_ANCHOR_LINK, 0)

        self.page.wait_for_timeout(2000)

        text_active_anchor = self.get_text(NewsLocators.NEWS_ANCHOR_LINK_ACTIVE, 0).split()
        text_media_badge = self.get_text(NewsLocators.NEWS_MEDIA_BADGE, 0).split()
        self.assertions.check_equals(text_link_news, text_active_anchor, '')
        self.assertions.check_equals(text_link_news, text_media_badge, '')

        self.click(NewsLocators.NEWS_TAB_NEW)