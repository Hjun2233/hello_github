import unittest
from ddt import ddt,data,unpack
from base_common.ExcelUtil import readExcel


@ddt
class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('连接数据库')

    @classmethod
    def tearDownClass(cls):
        print('关闭数据库')
        
    def setUp(self):
        print('打开浏览器')
    
    def tearDown(self):
        print('关闭浏览器')

    @data(*readExcel().read_excel())
    def test001(self, *loc):
        print('test001', *loc)
        
    @data(*readExcel().read_excel())
    @unpack
    def test002(self, xh, name, pwd):
        print('test002', xh, name, pwd)
        
if __name__ == '__main__':
    unittest.main()
