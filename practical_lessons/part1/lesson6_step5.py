from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    crypt = str(math.ceil(math.pow(math.pi, math.e)*10000))
    print(crypt)

    time.sleep(5)

    button = browser.find_element_by_partial_link_text(crypt)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла