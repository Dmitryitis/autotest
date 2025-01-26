import pytest
import testit
from pages.tenders import TendersPage

class TestTendersPage:
    @testit.workItemIds([43])
    @testit.displayName('Проверка поиска через поле "Введите ключевое слово или номер извещения"')
    def test_input_notice(self, browser):
        tender = TendersPage(browser)
        tender.check_input_notice()
    
    @testit.workItemIds([46])
    @testit.displayName('Проверка фильтрации по регионам')
    def test_check_filter_region(self, browser):
        tender = TendersPage(browser)
        tender.check_filter_by_region()

    @testit.workItemIds([45])
    @testit.displayName('Проверка фильтров сортировки')
    def test_check_sort_filter(self, browser):
        tender = TendersPage(browser)
        tender.check_select_sort()
    
    @testit.workItemIds([47])
    @testit.displayName('Проверка фильтров закупки По')
    def test_check_purchase(self, browser):
        tender = TendersPage(browser)
        tender.check_purchase_by_checkbox()

    @testit.workItemIds([48])
    @testit.displayName('Фильтр поиск по цене - ввод значений')
    def test_price_input(self, browser):
        tender = TendersPage(browser)
        tender.check_input_price()
    
    @testit.workItemIds([50])
    @testit.displayName('Проверка поиск по организаторам - введение значений')
    def test_search_organization(self, browser):
        tender = TendersPage(browser)
        tender.check_search_organization_input()
    
    @testit.workItemIds([52])
    @testit.displayName('Проверка фильтра поиск закупки')
    def test_method_of_purchase(self, browser):
        tender = TendersPage(browser)
        tender.check_method_of_purchase()

    @testit.workItemIds([53])
    @testit.displayName('Проверка фильтрации данных')
    def test_filter_tenders(self, browser):
        tender = TendersPage(browser)
        tender.check_filter_tenders()

    @testit.workItemIds([54])
    @testit.displayName('Проверка сохраненных запросов')
    def test_save_query(self, browser):
        tender = TendersPage(browser)
        tender.check_save_query()
