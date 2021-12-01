from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element_by_xpath("//*[@id='book']").click()

    x_element = browser.find_element_by_xpath("//*[@id='input_value']")
    x = x_element.text
    result = calc(x)

    input_result = browser.find_element_by_xpath("//*[@id='answer']")
    input_result.send_keys(result)

    button_submit = browser.find_element_by_xpath("//*[@id='solve']")
    browser.execute_script('return arguments[0].scrollIntoView(true);', button_submit)
    button_submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
