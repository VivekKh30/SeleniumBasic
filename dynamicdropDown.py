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
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, 'autosuggest').send_keys('Ind')
time.sleep(2)
countries = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/a")
for country in countries:
    if country.text == "India":
        country.click()
        break

assert driver.find_element(By.ID, 'autosuggest').get_attribute('value') == 'India'
