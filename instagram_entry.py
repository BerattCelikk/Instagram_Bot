#THIS CODE PROVİDES YOU TO  ACCESS TO INSTAGRAM AUTOMATICALLY



import getpass
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def __init__(self, email, password):
        self.browser = webdriver.Chrome()
        self.email = email
        self.password = password

    def signin(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        email_input = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
        password_input = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")

        email_input.send_keys(self.email)
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)

email=input("Email: ")
password=getpass.getpass("Password: ")


instgrm = Instagram(email, password)
instgrm.signin()

input("Press Enter to close the browser")

instgrm.browser.quit()