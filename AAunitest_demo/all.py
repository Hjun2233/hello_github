import pytest

"""  ==========pytest默认命名规则，pytest.ini文件可以修改==============
1.py文件必须以test_开头，或者_test结尾
2.测试用例的py文件的类名,必须以Test开头
3.测试用例必须以test_开头(test也行？)
"""
import os



if __name__ == '__main__':
    pytest.main()
    os.system('allure generate ./temp -o ./report/reports --clean')
    
    os.system('allure open ./report/reports')#https://blog.csdn.net/weixin_42581308/article/details/122883671
                                            #pytest可以直接启动外部浏览器打开.html文件，但是eclipse不行(allure提供了两种解决方法，allure serve和allure open两个命令)
#     os.system('allure server ./temp')#直接可以处理和打开temp目录下的json文件            