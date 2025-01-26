
class NewsLocators:
    INPUT_SEARCH = '//div[@class="search search--offset-bottom"]//input'
    BUTTON_SEARCH = '//button[@class="form-input__ctrl btn"]'
    LOADER_404 = '//div[@class="loader loader--404"]//div[@class="loader__legend"]'
    CLEAR_BUTTON_SEARCH = '//button[@class="form-input__ctrl form-input__ctrl--clear btn"]'
    NEWS_TITLE = '//h3[@class="media__title h3"]'
    NEWS_TAB_MAIN = '//div[@class="tab__buttons"]//button[@title="Главное"]'
    NEWS_TAB_NEW = '//div[@class="tab__buttons"]//button[@title="Свежее"]'
    NEWS_ANCHOR_LINK = '//button[@class="nav-anchor__link"]'
    NEWS_ANCHOR_LINK_ACTIVE = '//button[@class="nav-anchor__link _active"]'
    NEWS_MEDIA_BADGE = '//div[@class="badge media__badge"]'