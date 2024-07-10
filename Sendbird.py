from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Key, Controller
import pyperclip
import time

op = webdriver.ChromeOptions()
op.add_experimental_option('detach',True)
driver = webdriver.Chrome(op)
driver.maximize_window()

#create user test 1
class CreateUser():
    def Create_user(self):
        driver.get("https://sendbird-uikit-react.netlify.app/url-builder")
        driver.find_element(By.XPATH,"//input[@name='appId']").send_keys("37C8DB25-8B44-435F-A528-5BA9B9965FD0")
        driver.find_element(By.XPATH,"//input[@name='userId']").send_keys("UserBird1")
        driver.find_element(By.XPATH,"//input[@name='nickname']").send_keys("UsrBird1")
        driver.find_element(By.XPATH,"//button[@class='sticky-bottom-button']").click()
        urltest = pyperclip.paste()
        driver.execute_script("window.open('');")
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        driver.get(urltest)
        time.sleep(5)

        #create user test 2
        windows = driver.window_handles
        driver.switch_to.window(windows[0])
        driver.refresh()
        driver.find_element(By.XPATH,"//input[@name='appId']").send_keys("37C8DB25-8B44-435F-A528-5BA9B9965FD0")
        driver.find_element(By.XPATH,"//input[@name='userId']").send_keys("UserBird2")
        driver.find_element(By.XPATH,"//input[@name='nickname']").send_keys("UsrBird2")
        driver.find_element(By.XPATH,"//button[@class='sticky-bottom-button']").click()
        urltest = pyperclip.paste()
        driver.execute_script("window.open('');")
        windows = driver.window_handles
        driver.switch_to.window(windows[2])
        driver.get(urltest)
        time.sleep(5)

#Create Group
class CreateGroup() :
    def Create_Group(self):        
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        driver.find_element(By.CSS_SELECTOR,".sendbird-icon-create > [xmlns='http://www.w3.org/2000/svg']").click()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='sendbird-modal__content']")))  
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR,".sendbird-add-channel__rectangle__chat-icon > [xmlns='http://www.w3.org/2000/svg']").click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR,".sendbird-checkbox[for='UserBird2'] > .sendbird-checkbox--checkmark").click()
        driver.find_element(By.XPATH,"//span[.='Create']").click()

        #change group name
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR,".sendbird-icon-info > [xmlns='http://www.w3.org/2000/svg']").click()
        driver.find_element(By.XPATH,"//span[@class='sendbird-label sendbird-label--button-1 sendbird-label--color-primary']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//input[@name='channel-profile-form__name']").clear()
        driver.find_element(By.XPATH,"//input[@name='channel-profile-form__name']").send_keys("Group Chat Bird")
        driver.find_element(By.XPATH,"//span[.='Save']").click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR,".sendbird-icon-close > [xmlns='http://www.w3.org/2000/svg']").click()
        time.sleep(5)
        
#send text, picture
class SendMessage():
    def Send_Message(self):
        driver.find_element(By.XPATH,"//div[@id='sendbird-message-input-text-field']").send_keys("how are you ?")
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR,".sendbird-icon-send > [xmlns='http://www.w3.org/2000/svg']").click()
        time.sleep(5)
        windows = driver.window_handles
        driver.switch_to.window(windows[2])
        time.sleep(5)
        driver.find_element(By.XPATH,"//div[@class='sendbird-channel-preview__content__lower']").click()
        driver.find_element(By.XPATH,"//div[@id='sendbird-message-input-text-field']").send_keys("Good")
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR,".sendbird-icon-send > [xmlns='http://www.w3.org/2000/svg']").click()
        time.sleep(5)
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        driver.find_element(By.CSS_SELECTOR,".sendbird-icon-attach > [xmlns='http://www.w3.org/2000/svg']").click()
        time.sleep(5)
        keyboard = Controller()
        keyboard.type("C:\\salad.jpg")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
                
        
#leave group
class LeaveGroup():
    def Leave_Group(self):
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR,".sendbird-icon-info > [xmlns='http://www.w3.org/2000/svg']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//div[@class='sendbird-channel-settings__panel-item sendbird-channel-settings__panel-item__leave-channel']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//span[.='Leave']").click()
        windows = driver.window_handles
        driver.switch_to.window(windows[2])
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR,".sendbird-icon-info > [xmlns='http://www.w3.org/2000/svg']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//div[@class='sendbird-channel-settings__panel-item sendbird-channel-settings__panel-item__leave-channel']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//span[.='Leave']").click()
        time.sleep(5) 
        driver.quit()        

user = CreateUser()
user.Create_user()

group = CreateGroup()
group.Create_Group()

message = SendMessage()
message.Send_Message()

leave = LeaveGroup()
leave.Leave_Group()