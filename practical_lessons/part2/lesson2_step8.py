from selenium import webdriver
import os
import time

link = "http://suninjuly.github.io/file_input.html"

current_dir = os.path.abspath(os.path.dirname(__file__))
txt_path = os.path.join(current_dir, 'text_for_lesson2_step8.txt')


try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath("//*[@placeholder='Enter first name']").send_keys('Ivan')
    input2 = browser.find_element_by_xpath("//*[@placeholder='Enter last name']").send_keys('Ivanov')
    input3 = browser.find_element_by_xpath("//*[@placeholder='Enter email']").send_keys('123@123.com')

    put_file = browser.find_element_by_xpath("//input[@id='file']").send_keys(txt_path)

    button_submit = browser.find_element_by_css_selector("button.btn")
    browser.execute_script('return arguments[0].scrollIntoView(true);', button_submit)
    button_submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
