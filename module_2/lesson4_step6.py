from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.implicitly_wait(5)
link = "http://suninjuly.github.io/cats.html"

try:
    browser.get(link)
    button = browser.find_element(By.ID, "button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
