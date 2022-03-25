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
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.LINK_TEXT, 'Shop').click()
phones = driver.find_elements(By.XPATH, "//*[@class ='col-lg-3 col-md-6 mb-3']")
print(len(phones))
for phone in phones:
    if phone.find_element(By.XPATH, 'div/div/h4').text == 'Blackberry':
        phone.find_element(By.XPATH, 'div/div/button').click()
        break

driver.find_element(By.XPATH, "//a[@class = 'nav-link btn btn-primary']").click()
driver.find_element(By.XPATH, "//button[@class = 'btn btn-success']").click()
driver.find_element(By.XPATH, "//input[@id = 'country']").send_keys("in")
WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class = 'suggestions']")))
countries = driver.find_elements(By.XPATH, "//div[@class = 'suggestions']/ul")

for country in countries:
    if country.text == 'India':
        country.click()
        break

time.sleep(1)
checkbox = driver.find_element(By.XPATH, "//input[@type= 'checkbox']")
driver.execute_script("arguments[0].click();", checkbox)
#driver.find_element(By.XPATH, "//input[@type= 'checkbox']").click()
driver.find_element(By.XPATH, "//input[@value = 'Purchase']").click()
time.sleep(1)
actual_Text = driver.find_element(By.XPATH, "//div[@class = 'alert alert-success alert-dismissible']").text
print(actual_Text)
assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in actual_Text
driver.get_screenshot_as_file("screen.png")
