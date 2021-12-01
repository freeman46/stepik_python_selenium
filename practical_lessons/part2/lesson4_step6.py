from selenium import webdriver
import time
import math

link = " http://suninjuly.github.io/cats.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_button = browser.find_element_by_id("button")

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
