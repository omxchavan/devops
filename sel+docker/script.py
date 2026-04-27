from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://localhost:8000")

# --------Test Case 1: Empty Input--------
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(1)

if "Fields cannot be empty" in driver.page_source:
    print("Empty Input Test Passed")
else:
    print("Empty Input Test Failed")

# --------Test Case 2: Invalid Input--------
driver.find_element(By.NAME, "username").send_keys("wrong")
driver.find_element(By.NAME, "password").send_keys("wrong")
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(1)

if "Invalid Credentials" in driver.page_source:
    print("Invalid Input Test Passed")
else:
    print("Invalid Input Test Failed")

# --------Test Case 3: Valid Input--------
    driver.find_element(By.NAME, "username").clear()
driver.find_element(By.NAME, "password").clear()

driver.find_element(By.NAME, "username").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("1234")
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(1)

if "Login Successful" in driver.page_source:
    print("Valid Input Test Passed")
else:
    print("Valid Input Test Failed")

driver.quit()