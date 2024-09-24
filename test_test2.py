
import allure
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.story("字节模块")
@allure.title("搜索结果正确")
@allure.description("结果符合关键词内容")
class TestZiJie:
    def test_day3(self):
        # 初始化浏览器
        self.driver = webdriver.Chrome()
        # 最大化窗口
        self.driver.maximize_window()
        # 设置隐式等待
        self.driver.implicitly_wait(5)
        # 进入字节网站
        self.driver.get("https://jobs.bytedance.com/")
        # 点击搜索框，输入搜索的关键词
        self.driver.find_element(By.CSS_SELECTOR, '.atsx-input.atsx-input-lg.search-input').send_keys("测试工程师")
        # 点击搜索按钮
        self.driver.find_element(By.CSS_SELECTOR, '.atsx-btn.sofiaBold.atsx-btn-primary.atsx-btn-circle').click()
        # 等待搜索结果出现
        self.driver.implicitly_wait(5)
        # 获取职位名称
        object1 = self.driver.find_element(By.CSS_SELECTOR, '.positionItem-title-text')
        self.driver.implicitly_wait(5)
        # 断言搜索的关键词在标题当中
        assert "测试工程师" in object1.text

