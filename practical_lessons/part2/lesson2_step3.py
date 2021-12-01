from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time

link = "http://suninjuly.github.io/selects1.html"


def summa(num1, num2):
    return str(num1 + num2)


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_xpath("//*[@id='num1']").text
    y = browser.find_element_by_xpath("//*[@id='num2']").text
    result = summa(int(x), int(y))

    print(result)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(result)

    button_submit = browser.find_element_by_css_selector("button.btn")
    button_submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
