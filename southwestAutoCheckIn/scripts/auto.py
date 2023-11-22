from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

class SouthwestCheckIn:
    def __init__(self, confirmation_num, first_name, last_name, number):
        self.confirmation_num = confirmation_num
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.driver = webdriver.Chrome()
        self.check_in_link = 'https://www.southwest.com/air/check-in/index.html'

    def check_in(self):
        self.driver.get(self.check_in_link)
        conf_input = self.driver.find_element(By.ID, 'confirmationNumber')
        first_name_input = self.driver.find_element(By.ID, 'passengerFirstName')
        last_name_input = self.driver.find_element(By.ID, 'passengerLastName')

        conf_input.send_keys(self.confirmation_num)
        first_name_input.send_keys(self.first_name)
        last_name_input.send_keys(self.last_name)

        check_in_btn = self.driver.find_element(By.ID, 'form-mixin--submit-button')
        check_in_btn.click()

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'air-check-in-review-results--check-in-button')))

        confirm_btn = self.driver.find_element(By.CLASS_NAME, 'air-check-in-review-results--check-in-button')

        confirm_btn.click()

    def send_pass(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'boarding-pass-options--button-text')))
        text_btn = self.driver.find_element(By.CLASS_NAME, "boarding-pass-options--button-text")
        text_btn.click()

        number_input = self.driver.find_element(By.ID, 'textBoardingPass')
        number_confirmation = self.driver.find_element(By.ID, 'textBoardingPassConfirmation')

        number_input.send_keys(self.number)
        number_confirmation.send_keys(self.number)

        confirm_btn = self.driver.find_element(By.ID, 'form-mixin--submit-button')
        confirm_btn.click()


if __name__ == '__main__':
    checker = SouthwestCheckIn(
        '4H8U46',  # confirmation number
        'Anshul',  # first name
        'Chelapurath',  # last name
        '4439035656')  # phone number
    checker.check_in()
    
    checker.send_pass()