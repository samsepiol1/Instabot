from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class InstagramBot:

    def __init__(self,username,password ):
        self.username= username
        self.password= password
        self.driver= webdriver.Chrome('C:/Users/Deus/Downloads/chromedriver.exe')
    def closerBrowser(self):
        self.driver.closr()
    def login(self):
        driver= self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        login_button=driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)
        user_name_eles=driver.find_element_by_xpath("//input[@name='username']")
        user_name_eles.clear()
        user_name_eles.send_keys(self.username)
        password_element= driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(2)
    def like_photos(self, hashtag):
        driver= self.driver
        driver.get("https://instagram.com/explore/tags/"+ hashtag+ "/")
        time.sleep(2)
        for i in range(1,3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
        hrefs=driver.find_elements_by_tag_name('a')
        pic_hfers=[elem.get_attribute('href') for elem in hrefs ]
        pic_hfers=[href for href in pic_hfers if hashtag in href]
        print(hashtag+ "fotos"+ str(len(pic_hfers)))
        for pic_hfer in pic_hfers:
            driver.get(pic_hfer)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                like_button= lambda: driver.find_element_by_xpath('//span[@aria-label="Like"]').click()
                like_button().click()
                time.sleep(10)
            except Exception as e:
                time.sleep(2)
    def View_Storie(self):
        driver=self.driver
        driver.get("https://www.instagram.com/stories/"+view_stor+ "/")
        time.sleep(2)
        
LucasIG=InstagramBot('Your_Account','Your_password')
LucasIG.login()
LucasIG.like_photos('newyork')
hashtags=['amazing','beautiful','adventure']
[LucasIG.like_photos(tag) for tag in hashtags ]
view_stor='tribunadonorte'
LucasIG.View_Storie()

