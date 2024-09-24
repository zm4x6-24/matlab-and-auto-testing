from asyncio import sleep
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def test_day3():
    # 初始化浏览器
    driver = webdriver.Chrome()
    # 最大化页面
    driver.maximize_window()
    # 打开的网页
    driver.implicitly_wait(5)

    driver.get("https://jobs.bytedance.com/")

    # 找到搜索窗然后输入文本
    driver.find_element(By.CSS_SELECTOR, 'atsx-input.atsx-input-lg.search-input').send_keys("测试工程师")
    # 寻找搜索按钮，并点击
    driver.find_element(By.CSS_SELECTOR, 'atsx-btn sofiaBold atsx-btn-primary atsx-btn-circle').click()
    sleep(5)
    # 断言搜索结果的标题是否符合搜索的关键词
    # oppo1 = driver.find_element(By.CSS_SELECTOR, 'positionItem-title-text')
    # assert "测试工程师" in oppo1.text
    job_ele = driver.find_element(By.CSS_SELECTOR, '.positionItem-title-text')
    sleep(5)
    # 断言搜索的关键词在标题当中
    assert "测试工程师" in job_ele.text
'''
from asyncio import sleep
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_job_title():
    # 初始化浏览器
    driver = webdriver.Chrome()
    # 最大化窗口
    driver.maximize_window()
    # 设置隐式等待
    driver.implicitly_wait(5)
    # 进入字节招聘网站
    driver.get("https://jobs.bytedance.com/")
    # 点击搜索框，输入搜索的关键词
    driver.find_element(By.CSS_SELECTOR, '.atsx-input.atsx-input-lg.search-input').send_keys("测试工程师")
    # 点击搜索按钮
    driver.find_element(By.CSS_SELECTOR, '.atsx-btn.sofiaBold.atsx-btn-primary.atsx-btn-circle').click()
    # 等待搜索结果出现
    sleep(5)
    # 获取职位名称
    job_ele = driver.find_element(By.CSS_SELECTOR, '.positionItem-title-text')
    sleep(5)
    # 断言搜索的关键词在标题当中
    assert "测试工程师" in job_ele.text
'''