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

    def check_purchase_by_checkbox(self):
        self.open('tenders')

        self.assertions.check_URL('tenders', "Wrong URL")

        self.page.wait_for_timeout(2000)

        self.click_element_by_index(TendersLocators.TENDER_PURCHASE_BY_CHECKBOX, 1)
        self.assertions.check_box_activated(TendersLocators.TENDER_PURCHASE_BY_CHECKBOX,1, '')
        self.click_element_by_index(TendersLocators.TENDER_PURCHASE_BY_CHECKBOX, 2)
        self.assertions.check_box_activated(TendersLocators.TENDER_PURCHASE_BY_CHECKBOX,2, '')
        self.click_element_by_index(TendersLocators.TENDER_PURCHASE_BY_CHECKBOX, 3)
        self.assertions.check_box_activated(TendersLocators.TENDER_PURCHASE_BY_CHECKBOX,3, '')
        self.click_element_by_index(TendersLocators.TENDER_PURCHASE_BY_CHECKBOX, 4)
        self.assertions.check_box_activated(TendersLocators.TENDER_PURCHASE_BY_CHECKBOX,4, '')
        self.click_element_by_index(TendersLocators.TENDER_PURCHASE_BY_CHECKBOX, 5)
        self.assertions.check_box_activated(TendersLocators.TENDER_PURCHASE_BY_CHECKBOX,5, '')

        self.click(TendersLocators.TENDER_PURCHASE_BY_CHECKBOX_CLEAR)

        self.assertions.check_box_not_activated(TendersLocators.TENDER_PURCHASE_BY_CHECKBOX,1, '')

    def check_input_price(self):
        self.open('tenders')

        self.assertions.check_URL('tenders', "Wrong URL")

        self.page.wait_for_timeout(2000)

        self.input(TendersLocators.TENDER_PRICE_INPUT_BEFORE, '-100')
        text = self.get_text_from_input(TendersLocators.TENDER_PRICE_INPUT_BEFORE)
        self.assertions.check_equals(text,'', '')

        self.input(TendersLocators.TENDER_PRICE_INPUT_BEFORE, 'fdf@##@$')
        text = self.get_text_from_input(TendersLocators.TENDER_PRICE_INPUT_BEFORE)
        self.assertions.check_equals(text,'', '')

        self.input(TendersLocators.TENDER_PRICE_INPUT_BEFORE, '34')
        text = self.get_text_from_input(TendersLocators.TENDER_PRICE_INPUT_BEFORE)
        self.assertions.check_equals(text,'34', '')

        self.input(TendersLocators.TENDER_PRICE_INPUT_BEFORE, '34.5')
        text = self.get_text_from_input(TendersLocators.TENDER_PRICE_INPUT_BEFORE)
        self.assertions.check_equals(text,'34.5', '')

        self.input(TendersLocators.TENDER_PRICE_INPUT_BEFORE, '34.55')
        text = self.get_text_from_input(TendersLocators.TENDER_PRICE_INPUT_BEFORE)
        self.assertions.check_equals(text,'34.55', '')

        self.input(TendersLocators.TENDER_PRICE_INPUT_BEFORE, '34.555')
        text = self.get_text_from_input(TendersLocators.TENDER_PRICE_INPUT_BEFORE)
        self.assertions.check_equals(text,'34.55', '')
    
    def check_search_organization_input(self):
        self.open('tenders')

        self.assertions.check_URL('tenders', "Wrong URL")

        self.page.wait_for_timeout(2000)

        self.input(TendersLocators.TENDER_SEARCH_ORGANIZATION, '№;”,;%:№-+')
        text = self.get_text_from_input(TendersLocators.TENDER_SEARCH_ORGANIZATION)
        self.assertions.check_equals(text,'', '')

        self.input(TendersLocators.TENDER_SEARCH_ORGANIZATION, 'fsdfsf')
        text = self.get_text_from_input(TendersLocators.TENDER_SEARCH_ORGANIZATION)
        self.assertions.check_equals(text,'', '')

        self.input(TendersLocators.TENDER_SEARCH_ORGANIZATION, '1234567890')
        text = self.get_text_from_input(TendersLocators.TENDER_SEARCH_ORGANIZATION)
        self.assertions.check_equals(text,'1234567890', '')

        self.input(TendersLocators.TENDER_SEARCH_ORGANIZATION, '123456789012')
        text = self.get_text_from_input(TendersLocators.TENDER_SEARCH_ORGANIZATION)
        self.assertions.check_equals(text,'1234567890', '')
    

    def check_method_of_purchase(self):
        self.open('tenders')

        self.assertions.check_URL('tenders', "Wrong URL")

        self.page.wait_for_timeout(2000)

        self.click_element_by_index(TendersLocators.TENDER_FILTER_BUTTON, 0)

        text_all = self.get_text(TendersLocators.TENDER_LIST_CHECKBOX, 0)

        self.input(TendersLocators.TENDER_MODAL_INPUT, 'За')
        text_first_list_el = self.get_text(TendersLocators.TENDER_LIST_CHECKBOX, 0)
        self.assertions.check_not_equals(text_first_list_el, text_all, '')

        self.input(TendersLocators.TENDER_MODAL_INPUT, '')
        self.click_element_by_index(TendersLocators.TENDER_LIST_CHECKBOX, 0)

        self.click_element_by_index(TendersLocators.TENDER_MODAL_FOOTER_BUTTONS, 1)

        self.assertions.check_presence(TendersLocators.TENDER_FILTER_LIST, '')

        self.click_element_by_index(TendersLocators.TENDER_FILTER_BUTTON, 0)
        self.click_element_by_index(TendersLocators.TENDER_MODAL_FOOTER_BUTTONS, 0)

        self.assertions.check_absence(TendersLocators.TENDER_FILTER_LIST, '')

    def check_filter_tenders(self):
        self.open('tenders')

        self.assertions.check_URL('tenders', "Wrong URL")

        self.page.wait_for_timeout(2000)

        text_found_before = self.get_text(TendersLocators.COUNT_FOUND_TENDERS, 0).strip()

        self.click_element_by_index(TendersLocators.TENDER_PURCHASE_BY_CHECKBOX, 0)
        self.assertions.check_box_activated(TendersLocators.TENDER_PURCHASE_BY_CHECKBOX,0, '')

        self.click_element_by_index(TendersLocators.TENDER_PURCHASE_BY_CHECKBOX, 1)
        self.assertions.check_box_activated(TendersLocators.TENDER_PURCHASE_BY_CHECKBOX,1, '')
        self.click_element_by_index(TendersLocators.TENDER_PURCHASE_BY_CHECKBOX, 2)
        self.assertions.check_box_activated(TendersLocators.TENDER_PURCHASE_BY_CHECKBOX,2, '')

        self.input(TendersLocators.TENDER_SEARCH_ORGANIZATION, '1234567890')
        text = self.get_text_from_input(TendersLocators.TENDER_SEARCH_ORGANIZATION)
        self.assertions.check_equals(text,'1234567890', '')


        self.click_element_by_index(TendersLocators.TENDER_FILTER_BUTTON, 0)


        self.input(TendersLocators.TENDER_MODAL_INPUT, '')
        self.click_element_by_index(TendersLocators.TENDER_LIST_CHECKBOX, 1)

        self.click_element_by_index(TendersLocators.TENDER_MODAL_FOOTER_BUTTONS, 1)

        self.click(TendersLocators.TENDER_SEARCH_ACCEPT)

        self.page.wait_for_timeout(2000)

        text_found_after = self.get_text(TendersLocators.COUNT_FOUND_TENDERS, 0).strip()

        self.assertions.check_not_equals(text_found_before,text_found_after, '')

        self.click_element_by_index(TendersLocators.TENDER_SEARCH_FOOTER_BUTTONS, 0)

        self.page.wait_for_timeout(2000)

        text_found_after = self.get_text(TendersLocators.COUNT_FOUND_TENDERS, 0).strip()

        self.assertions.check_equals(text_found_before,text_found_after, '')
    
    def check_save_query(self):
        self.open('tenders')

        self.assertions.check_URL('tenders', "Wrong URL")

        self.page.wait_for_timeout(2000)

        counter_query = self.get_text(TendersLocators.TENDER_COUNTER_SAVE_QUERY, 0)
        text_found_before = self.get_text(TendersLocators.COUNT_FOUND_TENDERS, 0).strip()

        self.click_element_by_index(TendersLocators.TENDER_PURCHASE_BY_CHECKBOX, 0)
        self.assertions.check_box_activated(TendersLocators.TENDER_PURCHASE_BY_CHECKBOX,0, '')

        self.click_element_by_index(TendersLocators.TENDER_PURCHASE_BY_CHECKBOX, 1)
        self.assertions.check_box_activated(TendersLocators.TENDER_PURCHASE_BY_CHECKBOX,1, '')
        self.click_element_by_index(TendersLocators.TENDER_PURCHASE_BY_CHECKBOX, 2)
        self.assertions.check_box_activated(TendersLocators.TENDER_PURCHASE_BY_CHECKBOX,2, '')

        self.input(TendersLocators.TENDER_SEARCH_ORGANIZATION, '1234567890')
        text = self.get_text_from_input(TendersLocators.TENDER_SEARCH_ORGANIZATION)
        self.assertions.check_equals(text,'1234567890', '')


        self.click_element_by_index(TendersLocators.TENDER_FILTER_BUTTON, 0)


        self.input(TendersLocators.TENDER_MODAL_INPUT, '')
        self.click_element_by_index(TendersLocators.TENDER_LIST_CHECKBOX, 1)

        self.click_element_by_index(TendersLocators.TENDER_MODAL_FOOTER_BUTTONS, 1)

        self.click_element_by_index(TendersLocators.TENDER_SEARCH_FOOTER_BUTTONS, 1)

        self.click(TendersLocators.TENDER_SUCCESS_MODAL_BUTTON)

        new_counter = int(counter_query) + 1

        self.assertions.check_equals(int(counter_query) + 1, new_counter, '')

        self.click(TendersLocators.TENDER_OPEN_SAVE_QUERY)

        self.click_element_by_index(TendersLocators.TENDER_LIST_SAVE_QUERY, 0)

        self.click_element_by_index(TendersLocators.TENDER_MODAL_FOOTER_BUTTONS, 1)

        self.click(TendersLocators.TENDER_SEARCH_ACCEPT)

        self.page.wait_for_timeout(2000)

        text_found_after = self.get_text(TendersLocators.COUNT_FOUND_TENDERS, 0).strip()

        self.assertions.check_not_equals(text_found_before,text_found_after, '')

        self.click(TendersLocators.TENDER_OPEN_SAVE_QUERY)
        
        self.click_element_by_index(TendersLocators.TENDER_MODAL_FOOTER_BUTTONS, 0)

        self.assertions.check_equals(int(counter_query), new_counter - 1, '')


