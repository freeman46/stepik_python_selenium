import pytest
import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


class TestSecretText():
    id_for_link = [
        "236895",
        "236896",
        "236897",
        "236898",
        "236899",
        "236903",
        "236904",
        "236905"
    ]

    @pytest.mark.parametrize('id', id_for_link)
    def test_check_correct_message(self, browser, id):
        link = f'https://stepik.org/lesson/{id}/step/1'
        browser.get(link)
        answer = math.log(int(time.time()))
        browser.find_element_by_xpath('//textarea').send_keys(str(answer))
        submit_button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@class="submit-submission"]'))
        )
        submit_button.click()
        visible_message = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@class="smart-hints__hint"]'))
        )
        message_text = browser.find_element_by_xpath('//*[@class="smart-hints__hint"]').text
        print(message_text)
        print(type(message_text))
        assert message_text == "Correct!", f'Актуальное значение: {message_text}'
