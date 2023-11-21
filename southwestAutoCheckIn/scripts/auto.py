from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get ("https://www.southwest.com/air/check-in/index.html")

confirmationNumber = driver.find_element(By.ID, "confirmationNumber")
firstName = driver.find_element(By.ID, "passengerFirstName")
lastName = driver.find_element(By.ID, "passengerLastName")

confirmationNumber.send_keys('TestNum')
firstName.send_keys('Y')
lastName.send_keys('Cubed')

submit = driver.find_element(By.ID, 'form-mixin--submit-button')
confirm = driver.find_element(By.CLASS_NAME, 'air-check-in-review-results--check-in-button')
confirm.click()
text_btn = driver.find_element(By.CLASS_NAME, 'boarding-pass-options--button-text')
text_btn.click()
phone = driver.find_element(By.ID, 'textBoardingPass')
phone_conf = driver.find_element(By.ID, 'textBoardingPassConfirmation')
phone.send_keys('1234567890')
phone_conf.send_keys('1234567890')
confirm_btn = driver.find_element(By.ID, 'form-mixin--submit-button')
confirm_btn.click()
submit.click()