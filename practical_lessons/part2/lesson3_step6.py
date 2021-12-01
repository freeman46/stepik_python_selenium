from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_button = browser.find_element_by_css_selector("button.btn").click()

    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]

    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_xpath("//*[@id='input_value']")
    x = x_element.text
    result = calc(x)

    input_result = browser.find_element_by_xpath("//*[@id='answer']")
    input_result.send_keys(result)

    button_submit = browser.find_element_by_css_selector("button.btn")
    browser.execute_script('return arguments[0].scrollIntoView(true);', button_submit)
    button_submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
