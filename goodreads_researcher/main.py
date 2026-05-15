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

def scrape():

    driver = webdriver.Edge() 
    driver.get(user_link)
    time.sleep(2)
    driver.quit()

scrape()
