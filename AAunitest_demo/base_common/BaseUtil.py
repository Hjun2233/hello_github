'''封装公用的方法'''
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InitBrowser():
#     '''浏览器的常用操作封装'''
#     def __init__(self, driver):
#         self.driver = driver
#         driver = webdriver.Chrome()
#         self.driver.implicitly_wait(15)
#         self.driver.get('http://106.75.177.248:8285/#/login')
#     def wait_element_visible(self,locate):
#         '''显示等待元素'''
#         element = WebDriverWait(self.web, 10).until(EC.visibility_of_element_located(locate))
#         return element
    def click(self,locate):
        '''点击之前自动调用等待方法'''
        self.wait_element_visible(locate).click()
 
    def send_kyes(self,locate,value):
        '''输入之前，自动调用等待时间方法'''
        print(locate,value)
        self.wait_element_visible(locate).send_keys(value)
