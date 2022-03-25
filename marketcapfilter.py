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
driver.get("https://coinmarketcap.com/")
driver.find_element(By.XPATH, "(//*[@class='x0o17e-0 ewuQaX sc-36mytl-0 bBafzO table-control-filter'])[2]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//button[contains(., 'Add Filter')]").click()
filer_list = driver.find_elements(By.XPATH, "//*[contains(@class, 'cmc-filter-button')]")
for filter in filer_list:
    if filter.text == 'Market Cap':
        filter.click()
        break

market_cap_filter = driver.find_elements(By.XPATH, "//div[@class='cmc-filter-presets']//child::button")
for market_cap in market_cap_filter:
    if market_cap.text == '$100M - $1B':
        market_cap.click()
        break

for filter in filer_list:
    if filter.text == 'Price':
        filter.click()
        break

time.sleep(2)

price_filter = driver.find_elements(By.XPATH, "//div[@class='cmc-filter-presets']//child::button")

time.sleep(2)
for price in price_filter:
    if '$101 - $1,000' in price.text:
        price.click()
        break

driver.find_element(By.XPATH, "//button[@class='x0o17e-0 cEEOTh cmc-filter-button']").click()
driver.find_element(By.XPATH, "//button[@class='x0o17e-0 lgnbfA cmc-filter-button']").click()

time.sleep(3)
filter_result = driver.find_elements(By.XPATH, "//tbody/tr/td[4]")
# print(len(filter_result))

for values in filter_result:
    #print(values.text[1:])
    assert 100 < float(values.text[1:]) < 1000
