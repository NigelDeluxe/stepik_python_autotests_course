from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"

try:
    browser.get(link)
    first_name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    first_name.send_keys("Nigel")
    last_name = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    last_name.send_keys("Deluxe")
    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys("nigel_deluxe@miami.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "new_text_document.txt"
    file_path = os.path.join(current_dir, file_name)
    upload_file = browser.find_element(By.ID, "file")
    upload_file.send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
