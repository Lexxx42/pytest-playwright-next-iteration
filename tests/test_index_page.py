import pytest
import pages


class TestFooter:

    @pytest.mark.case_id(1)  # 1 - test ID from Qase
    def test_user_button_google_search_must_have_text_google_search(self, page):
        pages.index_page.open_index_page(page)
        pages.index_page.press_link_english_lang(page)
        actual_result = pages.index_page.get_text_from_google_search_button(page)
        assert actual_result == 'Google Search', 'Google Search button text is not correct'
