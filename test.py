from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from django.contrib.auth.models import User
import time
import django

class Hosttest(LiveServerTestCase):
  	
		def testhomepage(self):

				options = Options()
				options.headless = True
				driver = webdriver.Chrome(executable_path="/Users/mueezkhan/django-test/chromedriver", options=options)

				driver.get(self.live_server_url)
				# try driver.get(self.live_server_url) if driver.get('http://127.0.0.1:8000/') does not work
				
				assert "Hello, world!" in driver.title

# class LoginFormTest(LiveServerTestCase):

    
#     port = 8000
#     host = '127.0.0.1'
#     def setUp(self):
#         self.selenium = webdriver.Chrome(executable_path="/Users/mueezkhan/django-test/chromedriver")
#         super(LoginFormTest, self).setUp()
        
#     def tearDown(self):
#         self.selenium.quit()
#         super(LoginFormTest, self).tearDown()
    
#     def testform(self):
#         driver = self.selenium
#     #     super(LoginFormTest, self).setUp()
#         driver.get(f"http://127.0.0.1:8000/accounts/login")

#         # user = User.objects.create_user('kamil', 'lennon@thebeatles.com', 'kamil')

#         # print(user)
#         # time.sleep(1)
#         user_name = driver.find_element_by_name('username')
#         user_password = driver.find_element_by_name('password')
#         time.sleep(3)
#         submit = driver.find_element_by_id('submit')

#         user_name.send_keys('kamil')
#         user_password.send_keys('kamil')

#         submit.send_keys(Keys.RETURN)
#         time.sleep(3)
#         print(driver.page_source)
#         assert 'kamil' in driver.page_source 
      