import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import math
import credential

task_answer = []


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('lesson', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_feedback_text(browser, lesson):
    link = f"https://stepik.org/lesson/{lesson}/step/1"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, ".navbar__auth_login").click()
    browser.find_element(By.ID, "id_login_email").send_keys(credential.stepik_login)
    browser.find_element(By.ID, "id_login_password").send_keys(credential.stepik_password)
    browser.find_element(By.CSS_SELECTOR, ".sign-form__btn").click()
    time.sleep(10)
    answer = math.log(int(time.time()))
    browser.find_element(By.CSS_SELECTOR, ".string-quiz__textarea").send_keys(str(answer))
    WebDriverWait(browser, 5).until(ec.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))).click()
    try:
        browser.find_element(By.CSS_SELECTOR, ".again-btn").click()
    finally:
        feedback = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
        if feedback.text != "Correct!":
            task_answer.append(feedback.text)
        assert feedback.text == "Correct!", "Optional feedback text is not 'Correct!'"


def test_print_answer():
    print(''.join(task_answer))


if __name__ == "__main__":
    pytest.main()
