from data.assertions import Assertions
from pages.base import Base
from locators.TendersPage import TendersLocators

class TendersPage(Base):
    def __init__(self, page):
        super().__init__(page)
        self.assertions = Assertions(page)
    
    def check_input_notice(self):
        self.open('tenders')

        self.assertions.check_URL('tenders', "Wrong URL")

        self.input(TendersLocators.INPUT_NOTICE, 'fdsfsdsgsgsgfgfs')
        self.click(TendersLocators.BUTTON_SEARCH)
        self.page.wait_for_timeout(2000)
        text_not_found = self.get_text(TendersLocators.LOADER_404, 0).strip()

        self.assertions.check_equals(text_not_found, 'Ничего не найдено', 'Invalid')
        
        self.click(TendersLocators.CLEAR_BUTTON_SEARCH)
        self.input(TendersLocators.INPUT_NOTICE, '0358300354425000001')
        self.click_enter()
        self.page.wait_for_timeout(2000)
        text_found = self.get_text(TendersLocators.COUNT_FOUND_TENDERS, 0).strip()

        self.assertions.check_equals(text_found, 'Найдена 1 запись.', 'Invalid')