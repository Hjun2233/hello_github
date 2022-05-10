from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import unittest
from selenium.webdriver.common.by import By
from ddt import ddt,data,unpack
from base_common.ExcelUtil import readExcel
 
 

@ddt
class testIdus(unittest.TestCase):

 
    def setUp(self):
        global driver
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.get('http://106.75.177.248:8285/#/login')
         
    @data(*readExcel().read_excel())
    @unpack
    def test_i(self, xh, name, pwd):
        print(xh, name, pwd)
        self.driver.find_element(By.XPATH, "//input[@placeholder='账号']").send_keys()
        self.driver.find_element(By.XPATH, "//input[@placeholder='密码']").send_keys()
        self.driver.find_element(By.XPATH, "//span[text()='登录']").click()
        if xh == 1:
            print('1laile!')
        elif xh == 2:
            print('2laile!')
        elif xh == 3:
            print('3laile!')
         
         
    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()
