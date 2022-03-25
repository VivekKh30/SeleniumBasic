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
driver.find_element(By.XPATH, "(//div[@class='sc-16r8icm-0 tu1guj-0 cSTqvK'])[1]").click()
time.sleep(1)
rowCount = driver.find_elements(By.XPATH, "//button[@class = 'x0o17e-0 bnhhNH']")
for row in rowCount:
    if row.text == '50':
        row.click()
        break

time.sleep(2)
rowList = driver.find_elements(By.XPATH, "//table[@class='h7vnx2-2 czTsgW cmc-table  ']/tbody/tr")
print(len(rowList))
assert len(rowList) == 50



