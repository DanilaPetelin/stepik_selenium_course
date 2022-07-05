from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

def solve_task(browzer):
    input_value = int(browzer.find_element(By.ID,"input_value").text)
    answer = calc(input_value)  #ln(abs(12*sin(x)))
    browzer.find_element(By.ID, "answer").send_keys(answer)
    browzer.find_element(By.CSS_SELECTOR, "button[type = 'submit']").click()


try:
    browser = webdriver.Chrome()
    # browser.implicitly_wait(time_to_wait=5)
    link ="http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element(
             (By.ID, "price"), '$100'
        )
    )
    browser.find_element(By.ID, 'book').click()

    solve_task(browser)

finally:
    sleep(5)
    browser.quit()