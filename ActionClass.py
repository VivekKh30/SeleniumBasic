import time
import selenium
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("start-maximized")
chrome_options.add_experimental_option("detach", True)
d = DesiredCapabilities.CHROME
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options, desired_capabilities=d)
driver.maximize_window()
print(driver.title)
# driver.implicitly_wait(5)
'''driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()'''

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver)
# action.context_click(driver.find_element(By.ID, "double-click")).perform()
action.double_click(driver.find_element(By.ID, "double-click")).perform()
alert = driver.switch_to.alert
assert "You double clicked me!!!, You got to be kidding me" == alert.text
alert.accept()
