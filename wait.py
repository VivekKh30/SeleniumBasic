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
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, 'input.search-keyword').send_keys("ber")
time.sleep(2)
assert len(driver.find_elements(By.XPATH, "//div[@class= 'product']")) == 3
buttons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
print(len(buttons))

list = []

for button in buttons:
    list.append(button.find_element(By.XPATH, 'parent::div/parent::div/h4').text)
    button.click()

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
list1 = []
time.sleep(1)
vegiee = driver.find_elements(By.CSS_SELECTOR, 'p.product-name')

for veg in vegiee:
    list1.append(veg.text)

print(list1)

# assert list == list1
WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'promoCode')))
driver.find_element(By.CLASS_NAME, 'promoCode').send_keys('rahulshettyacademy')
driver.find_element(By.CLASS_NAME, 'promoBtn').click()
WebDriverWait(driver, 6).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'promoInfo')))
assert driver.find_element(By.CLASS_NAME, 'promoInfo').text == 'Code applied ..!'
# WebDriverWait(driver, 6).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'promoInfo')))

total_prices = driver.find_elements(By.XPATH, "//tbody/tr/td[5]")
sum = 0.0
for price in total_prices:
    sum = sum + float(price.text)

actual_price = float(driver.find_element(By.CLASS_NAME, 'discountAmt').text)
discount = driver.find_element(By.CLASS_NAME, 'discountPerc').text
dis = int(discount[0:len(discount) - 1])
print(sum, actual_price)
assert sum-(sum * dis / 100) == actual_price
