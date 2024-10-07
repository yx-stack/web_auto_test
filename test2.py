import allure
class Test_001:
    @allure.step(title="这是一个测试步骤1")
    def test_001_1(self):
        print("----.test_001_1")
        assert True
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step(title="这是一个测试步骤1")
    def test_001_1(self):
        allure.attach("标题","具体内容")
        print("----.test_001_1")
        assert  True
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step(title="这是一个测试步骤2")
    def test_001_2(self):
        print("----.test_001_2")
        assert  True
    @allure.severity(allure.severity_level.NORMAL)
    @allure.step(title="这是一个测试步骤3")
    def test_001_3(self):
        print("----.test_001_3")
        assert True
    @allure.severity(allure.severity_level.MINOR)
    @allure.step(title="这是一个测试步骤4")
    def test_001_4(self):
        print("----.test_001_4")
        assert True
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.step(title="这是一个测试步骤5")
    def test_001_5(self):
        print("----.test_001_5")
        assert True