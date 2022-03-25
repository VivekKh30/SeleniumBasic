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
chrome_options.add_argument("headless")
chrome_options.add_experimental_option("detach", True)
d = DesiredCapabilities.CHROME
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options, desired_capabilities=d)
driver.maximize_window()
print(driver.title)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME, "name").send_keys("hello")
print(driver.find_element(By.NAME, "name").text)
print(driver.find_element(By.NAME, "name").get_attribute("value"))
print(driver.execute_script('return document.getElementsByName("name")[0].value'))
shopButton = driver.find_element(By.CSS_SELECTOR, "a[href*='shop']")
driver.execute_script("arguments[0].click();", shopButton)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
