import config
from playwright.sync_api import Page


class IndexPage:
    _BUTTON_GOOGLE_SEARCH = "//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']"
    _LINK_ENGLISH_LANG = "//a[contains(text(), 'English')]"

    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)

    def press_link_english_lang(self, page: Page):
        page.locator(self._LINK_ENGLISH_LANG).click()

    def get_text_from_google_search_button(self, page: Page):
        return page.locator(self._BUTTON_GOOGLE_SEARCH).get_attribute('value')

        # page - the page: https://google.com
        # locator(self._BUTTON_GOOGLE_SEARCH) - finds the element
        # .get_attribute('value') - gets the attribute value from the element
