import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# https://stackoverflow.com/questions/76461596/unable-to-use-selenium-webdriver-getting-two-exceptions
# This is due to changes in Selenium 4.10

service = Service(executable_path=r"C:\\Users\\Paulinha\\BPCE-IT Exercise\\chromedriver.exe")

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service)
driver.maximize_window()
try:
    driver.get("https://www.banquepopulaire.fr/")
except:
    print('Site not found')

wait = WebDriverWait(driver, 5)
try:
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="consent_prompt_submit"]'))).click()
    print('Successfully Accepted Cookies')
except:
    print('Could not click')
    pass