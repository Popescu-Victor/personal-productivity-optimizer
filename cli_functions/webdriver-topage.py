from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options



def url_structure(url):
    if "www." and ".com" in url:
        return url
    else:
        full_url = "www." + str(url) + ".com"
        return full_url

def open_webpage(url)
    options = Options()
    driver = webdriver.Edge(options=options)
    driver.get(url)

    print("Page title:", driver.title)

    driver.quit()

