import time
import selenium
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
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
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, 'Click Here').click()
child = driver.window_handles[1]
driver.switch_to.window(child)
print(driver.find_element(By.TAG_NAME, 'h3').text)
assert driver.find_element(By.TAG_NAME, 'h3').text == 'New Window'
parent = driver.window_handles[0]
driver.switch_to.window(parent)
assert driver.find_element(By.TAG_NAME, 'h3').text == 'Opening a new window'
driver.get("https://the-internet.herokuapp.com/frames")
driver.find_element(By.LINK_TEXT, 'iFrame').click()
driver.switch_to.frame('mce_0_ifr')
driver.find_element(By.CLASS_NAME, 'mce-content-body ').clear()
driver.find_element(By.CLASS_NAME,'mce-content-body ').send_keys("in frame")
