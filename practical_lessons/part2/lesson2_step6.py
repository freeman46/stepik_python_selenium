from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath("//*[@id='input_value']")
    x = x_element.text
    result = calc(x)

    input_result = browser.find_element_by_xpath("//*[@id='answer']")
    input_result.send_keys(result)

    robo_option = browser.find_element_by_xpath("//*[@id='robotCheckbox']")
    robo_option.click()

    robo_rule = browser.find_element_by_xpath("//*[@id='robotsRule']")
    browser.execute_script('return arguments[0].scrollIntoView(true);', robo_rule)
    robo_rule.click()

    button_submit = browser.find_element_by_css_selector("button.btn")
    browser.execute_script('return arguments[0].scrollIntoView(true);', button_submit)
    button_submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла