from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_registration1(self):
        browser = self.browser
        browser.get("http://suninjuly.github.io/registration1.html")
        browser.implicitly_wait(5)
        browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Nigel")
        browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Deluxe")
        browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("nigel_deluxe@miami.com")
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        welcome_text_element = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_element.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_registration2(self):
        browser = self.browser
        browser.get("http://suninjuly.github.io/registration2.html")
        browser.implicitly_wait(5)
        browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Nigel")
        browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Deluxe")
        browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("nigel_deluxe@miami.com")
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        welcome_text_element = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_element.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
