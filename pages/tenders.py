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

        self.assertions.check_presence(TendersLocators.LOADER_404,'')
        
        self.click(TendersLocators.CLEAR_BUTTON_SEARCH)
        self.input(TendersLocators.INPUT_NOTICE, '0358300354425000001')
        self.click_enter()
        self.page.wait_for_timeout(2000)
        text_found = self.get_text(TendersLocators.COUNT_FOUND_TENDERS, 0).strip()

        self.assertions.check_equals(text_found, 'Найдена 1 запись.', 'Invalid')
    

    def check_filter_by_region(self):
        self.open('tenders')

        self.assertions.check_URL('tenders', "Wrong URL")

        self.click(TendersLocators.CHOOSE_REGION_BUTTON)

        self.page.wait_for_timeout(1000)

        self.input(TendersLocators.INPUT_REGION, '23')
        self.assertions.check_presence(TendersLocators.LOADER_404,'')

        self.click(TendersLocators.CLEAR_BUTTON_REGION)
        self.input(TendersLocators.INPUT_REGION, 'Алтайский')
        self.click(TendersLocators.ELEMENT_REGION)

        text_region= self.get_text(TendersLocators.CHOOSE_REGION_BUTTON, 0).strip()
        self.assertions.check_equals(text_region, 'в регионе Алтайский край', '')

    def check_select_sort(self):
        self.open('tenders')

        self.assertions.check_URL('tenders', "Wrong URL")

        self.click(TendersLocators.TENDER_SELECT_SORT)

        self.assertions.check_presence(TendersLocators.TENDER_SELECT_SORT_DROPDOWN, '')
        text_sort_choose = self.get_text(TendersLocators.TENDER_SELECT_SORT_BUTTON, 2).split()

        self.click_element_by_index(TendersLocators.TENDER_SELECT_SORT_BUTTON, 2)

        self.assertions.check_absence(TendersLocators.TENDER_SELECT_SORT_DROPDOWN, '')

        text_sort = self.get_text(TendersLocators.TENDER_SELECT_SORT, 0).split()

        self.assertions.check_equals(text_sort, text_sort_choose, '')