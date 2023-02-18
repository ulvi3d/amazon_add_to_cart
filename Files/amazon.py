import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class amazon():

    def add_to_cart(self):
        s = Service("D:\Drivers\chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        driver.implicitly_wait(10)

        driver.get("https://www.amazon.com/")
        driver.maximize_window()


        # search for asus laptop
        search_bar = driver.find_element(By.XPATH, "(//input[@id='twotabsearchtextbox'])[1]")
        search_bar.click()
        search_bar.send_keys("asus laptop")
        search_bar.send_keys(Keys.ENTER)

        # sort by Newest Arrivals
        driver.find_element(By.XPATH, "(//span[@class='a-dropdown-label'])[1]").click()
        driver.find_element(By.XPATH, "(//a[normalize-space()='Newest Arrivals'])[1]").click()

        # select second product from the list
        driver.find_element(By.PARTIAL_LINK_TEXT, "ASUS").click()

        # change the delivery country to US
        driver.find_element(By.ID, "contextualIngressPtPin").click()
        dropdown = driver.find_element(By.XPATH, "//span[@id='GLUXCountryValue']")
        actions = ActionChains(driver)
        actions.double_click(dropdown).perform()
        driver.find_element(By.ID, "GLUXCountryList_234").click()
        driver.refresh()

        # add to cart
        driver.find_element(By.XPATH, "//input[@id='add-to-cart-button']").click()
        driver.find_element(By.XPATH, "//input[@aria-labelledby='attachSiNoCoverage-announce']").click()
        driver.refresh()
        driver.find_element(By.XPATH, "//span[normalize-space()='Cart']").click()

        time.sleep(3)

start_test = amazon()
start_test.add_to_cart()