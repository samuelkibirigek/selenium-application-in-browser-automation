from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service("C:/Development/chromedriver.exe")

driver = webdriver.Chrome(service=service)

driver.get("https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Kalule Samuel")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Kibirige")

email_address = driver.find_element(By.NAME, "email")
email_address.send_keys("samuelkibirigek@gmail.com")
 
sign_up = driver.find_element(By.XPATH, "/html/body/form/button")
sign_up.send_keys(Keys.ENTER)


