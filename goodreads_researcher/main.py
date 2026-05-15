from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import dotenv
import os

def obtain_username(handle):
    link = "https://www.goodreads.com/user/show/" + str(handle)
    return link

def input_handle():
    user_handle = input("Paste the user handle here:   ")
    user_link = obtain_username(user_handle)
    return user_link

dotenv.load_dotenv(r'C:\Users\roman\Desktop\ERQL Github\productivity\personal-productivity-optimizer\goodreads_researcher\goodreads.env')
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")

print(str(LOGIN_EMAIL) + " " + str(LOGIN_PASSWORD))

def scrape():

    driver = webdriver.Edge() 
    driver.get("https://www.goodreads.com/user/sign_in")

    
    time.sleep(2)

    login_link = driver.find_element(By.CSS_SELECTOR, ".gr-button.gr-button--dark.gr-button--auth.authPortalConnectButton.authPortalSignInButton")
    login_link.click()
    time.sleep(2)
    
    print("Got to login by email")
    
    email_field = driver.find_element(By.ID, "ap_email")
    email_field.send_keys(LOGIN_EMAIL)
    
    password_field = driver.find_element(By.ID, "ap_password")
    password_field.send_keys(LOGIN_PASSWORD)
    password_field.send_keys(Keys.RETURN)

    user_link = input_handle()

    driver.get(user_link)
    
    time.sleep(2)
    link = driver.find_element(By.XPATH, "//a[contains(@href, 'rating&view=reviews')]")
    link.click()
    driver.quit()

scrape()