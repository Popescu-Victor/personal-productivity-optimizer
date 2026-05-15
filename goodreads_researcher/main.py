from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import dotenv
import os

def obtain_username(handle):
    link = "https://www.goodreads.com/user/show/" + str(handle)
    return link

user_handle = input("Paste the user handle here:   ")
user_link = obtain_username(user_handle)


USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

'rating&view=reviews'




def scrape():

    driver = webdriver.Edge() 
    driver.get("https://www.goodreads.com/user/sign_in")
    time.sleep(2)

    login_link = driver.find_element(By.CSS_SELECTOR, ".gr-button.gr-button--dark.gr-button--auth.authPortalConnectButton.authPortalSignInButton")
    login_link.click()
    time.sleep(2)
    
    driver.get(user_link)
    
    time.sleep(2)
    link = driver.find_element(By.XPATH, "//a[contains(@href, 'rating&view=reviews')]")
    link.click()
    driver.quit()

scrape()
