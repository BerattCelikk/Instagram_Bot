



import getpass
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options

class Instagram:
    def __init__(self, username, password):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        
        self.browser = webdriver.Chrome(options=chrome_options)
        self.username = username
        self.password = password

    def signin(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        username_input = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
        password_input = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")

        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)

    def unfollowUser(self,username):
        self.browser.get("https://www.instagram.com/"+username)
        time.sleep(2)
        
        follow_button=self.browser.find_element(By.TAG_NAME,"button")
        if follow_button.text == "following" or follow_button.text=="Takiptesin":
            follow_button.click()
            time.sleep(2)
            confirmation_button=self.browser.find_element(By.XPATH,"//button[text()='Takibi Bırak']")
            confirmation_button.click()
        else:
            print("already you unfollowed")
username=input("username: ")
password=getpass.getpass("Password: ")


instgrm = Instagram(username, password)
instgrm.signin()
unfollow=input("Who do you want to unfollow?")
instgrm.unfollowUser(unfollow)

input("Press Enter to close the browser")

instgrm.browser.quit()