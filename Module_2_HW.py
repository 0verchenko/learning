import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)


def calc(num):
    return str(math.log(abs(12*math.sin(int(num)))))


button = browser.find_element(By.ID, 'book')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '10000 RUR'))
button.click()
x = browser.find_element_by_css_selector('#input_value').text
math_ = calc(x)
browser.find_element_by_css_selector('#answer').send_keys(math_)
element = browser.find_element_by_css_selector('button[type="submit"]')
browser.execute_script("return arguments[0].scrollIntoView(true);", element)

browser.find_element_by_css_selector('button[type="submit"]').click()


# browser.quit()


