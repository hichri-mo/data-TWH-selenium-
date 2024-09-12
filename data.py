from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import dotenv
import os
dotenv.load_dotenv()


driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/login/fr?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

time.sleep(10)
# Wait for the page to load
username = driver.find_element(By.NAME, "session_key")
username.send_keys(os.environ["email"])
password = driver.find_element(By.NAME, "session_password")
password.send_keys(os.environ["password"])
#Click the login button
sing_clik=driver.find_element(By.CLASS_NAME, "login__form_action_container ")
sing_clik.click()

#now we move to scrap our data 
driver.get("https://www.linkedin.com/company/twensa-hosting-aihub/")
time.sleep(20)

# # moving to home 
# home=WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, ".org-page-navigation__item.m0.ml1"))
# )

# home.click()


# home_text = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, ".org-about-module__description"))
# )

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".update-components-text.relative.update-components-update-v2__commentary"))
)
print(element.text)

with open("scraped_data.txt", "w", encoding="utf-8") as f:
    f.write(element.text)
driver.quit()

