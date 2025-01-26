

class TendersLocators:
    INPUT_NOTICE_WRAPPER = '//div[@class="search__input form-input form-input--ctrl form-input--btn-clear"]'
    INPUT_NOTICE = "//div[@class='search__input form-input form-input--ctrl form-input--btn-clear']//input"
    INPUT_REGION = "//div[@class='form-input form-input--no-label form-input--ctrl']//input"
    BUTTON_SEARCH = '//button[@class="form-input__ctrl btn"]'
    CLEAR_BUTTON_SEARCH = '//button[@class="form-input__ctrl form-input__ctrl--clear btn"]'
    CLEAR_BUTTON_REGION = '//div[@class="modal__header-content"]//button'
    LOADER_404 = '//div[@class="loader loader--404"]//div[@class="loader__legend"]'
    COUNT_FOUND_TENDERS = '//div[@class="search__legend"]'
    CHOOSE_REGION_BUTTON = '//button[@class="mark-ctrl"]'
    ELEMENT_REGION = '//button[@class="dropdown__button"]'
    TENDER_SELECT_SORT = '//button[@class="select__body"]'
    TENDER_SELECT_SORT_BUTTON = '//button[@class="select__button"]'
    TENDER_SELECT_SORT_DROPDOWN = '//div[@class="select__dropdown"]'