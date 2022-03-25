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
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH, "(//input[@name='name'])[1]").send_keys("vivek")
print(driver.find_element(By.NAME, "email").send_keys("test@test.com"))
driver.find_element(By.ID, 'exampleCheck1').click()
dropdown = Select(driver.find_element(By.ID, 'exampleFormControlSelect1'))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Female")
# driver.find_element_by_class_name("btn btn-success").click()
driver.find_element(By.CSS_SELECTOR, "input[value='Submit']").click()
message = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
assert "Success" in message
