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

    def followUser(self,username):
        self.browser.get("https://www.instagram.com/"+username)
        time.sleep(2)
        
        followButton=self.browser.find_element(By.TAG_NAME,"button")
        if followButton.text != "Takiptesin" or followButton.text == "Follow":
            followButton.click()
            time.sleep(2)
        else:
            print("already following")
    
username=input("username: ")
password=getpass.getpass("Password: ")


instgrm = Instagram(username, password)
instgrm.signin()
follow=input("Who do you want to follow?")
instgrm.followUser(follow)

input("Press Enter to close the browser")

instgrm.browser.quit()