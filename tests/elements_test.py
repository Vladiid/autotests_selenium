import time

from configuration import TEXTBOX_URL, CHECKBOX_URL, RDIO_BUTTON_URL, BUTTONS_URL
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage


# ButtonsPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, TEXTBOX_URL)
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
            assert full_name == output_name
            assert email == output_email
            assert current_address == output_cur_addr
            assert permanent_address == output_per_addr
            time.sleep(2)

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, CHECKBOX_URL)
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, "checkboxes have not  been selected"
            time.sleep(5)

    class TestRadiButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, RDIO_BUTTON_URL)
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('Yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('Impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('No')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', "'Yes' have not been selected"
            assert output_impressive == 'Impressive', "'Impressive' have not been selected"
            assert output_no == 'No', "'No' have not been selected"

    # class TestButtonsPage:
    #     def test_different_click_on_the_buttons(self, driver):
    #         button_page = ButtonsPage(driver, BUTTONS_URL)
    #         button_page.open()
