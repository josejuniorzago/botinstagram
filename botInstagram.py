from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r'C:\JoseJr\geckodriver\geckodriver.exe')

    # //a[@href='/accounts/login/?source=auth_switcher']
    # //input[@name='username']
    # //input[@name='password']

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(2)
        #login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        #login_button.click()
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        self.curtir_fotos("memesbr")

    def curtir_fotos(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(5)
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        #hrefs = driver.find_elements_by_tag_name('a')
        hrefs = driver.find_elements_by_class_name("eLAPa")
        print(hashtag + ' fotos: ' + str(len(hrefs)))

        for href in hrefs:
            href.click()
            href.send_keys(Keys.ESCAPE)
            #driver.find_element_by_class_name("wpO6b").click()
            time.sleep(19)


        #pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        #[href for href in pic_hrefs if hashtag in href]
        #print(hashtag + ' fotos: ' + str(len(pic_hrefs)))

        #for pic_href in pic_hrefs:
        #    print(pic_href)
        #    driver.get(pic_href)
        #    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #    try:
        #        driver.find_element_by_class_name("//button[@class='wpO6b']").click()
        #        time.sleep(19)
        #    except Exception as e:
        #        time.sleep(5)



igBot = InstagramBot('jose@gmail.com', '12341rgafda')
igBot.login()
