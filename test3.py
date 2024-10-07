import os


import allure

class Test_003:
    @allure.step(title="这是一个测试步骤1")
    def test_003_1(self):
        with open(os.getcwd()+os.sep+"微信截图_20241003130601.png","rb") as f:
            allure.attach(f.read(),"微信截图_20241003130601.png",allure.attachment_type.PNG)
            assert True