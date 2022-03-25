import time

import selenium
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
chrome_options = Options()
chrome_options.add_argument("start-maximized")
chrome_options.add_experimental_option("detach", True)
d = DesiredCapabilities.CHROME
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options, desired_capabilities=d)
driver.maximize_window()
print(driver.title)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)
driver.find_element(By.NAME, 'enter-name').send_keys("option3")
driver.find_element(By.ID, 'alertbtn').click()
alert = driver.switch_to.alert
alert_text = alert.text
time.sleep(3)
alert.accept()
assert "option3" in alert_text
