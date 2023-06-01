import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


wd = webdriver.Chrome()
wd.implicitly_wait(10)

# wd0 = webdriver.Chrome()
# wd0.implicitly_wait(10)
# my_action=ActionChains(wd0)



wd.get('http://jwxk.hrbeu.edu.cn/xsxk/elective/grablessons?batchId=9de57c84469a42589b1bcf8b415251e5')#选课主页

wd.find_element(By.XPATH,'//*[@id="loginNameDiv"]/div/input').send_keys("2020108707")
wd.find_element(By.XPATH,'//*[@id="loginPwdDiv"]/div/input').send_keys("2020108707Nn")#输入账号密码

wd.find_element(By.XPATH,'//*[@id="verifyCode"]').send_keys("")#输入线会在验证码位置停留，输入验证码后把整个chromm窗口拉到最大
time.sleep(25)
wd.execute_script("arguments[0].click()", wd.find_element(By.XPATH,'//*[@id="loginDiv"]/button/span'))#登录
wd.execute_script("arguments[0].click()", wd.find_element(By.XPATH,'//*[@id="xsxkapp"]/div[4]/div/div[3]/span/button[1]'))

time.sleep(2)
wd.execute_script("arguments[0].click()", wd.find_element(By.XPATH,'//*[@id="stundentinfoDiv"]/button/span'))#进入
time.sleep(0.001)
wd.find_element(By.XPATH,"//html").click()#不重要的空白页点击跳过
time.sleep(2)
wd.execute_script("arguments[0].click()", wd.find_element(By.XPATH,'//*[@id="xsxkapp"]/div/div[1]/ul/li[3]/span'))#选择公选课一
wd.execute_script("arguments[0].click()", wd.find_element(By.XPATH,'//*[@id="xsxkapp"]/div/div[3]/div[2]/div[3]/div/div[2]/div/div/span/span/i'))#下拉ABCDEF类型选框
wd.execute_script("arguments[0].click()", wd.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[1]/ul/li[2]'))#选择F类
# time.sleep(1)
wd.find_element(By.XPATH,'//*[@id="xsxkapp"]/div/div[3]/div[2]/button').click()#点击搜索，界面更新
time.sleep(1)

has_chosen = []#这是已经选择的课程

while True:
#
    isend2 = 0#跳出循环
    lastpage_click = wd.find_element(By.XPATH,'//*[@id="xsxkapp"]/div/div[3]/div[3]/div/div[2]/ul/li[last()]')
    lastpage_click.click()#直接进入最后一页
    pages = int(lastpage_click.text)
    time.sleep(1)
    for page in range(pages):#进行逐页查询
        print("Page Searching...")
        isend1 = 0
        pagemean = page+1
        print(pagemean)
        wd.find_element(By.XPATH, "//*[@id='xsxkapp']/div/div[3]/div[3]/div/div[2]/ul/li[text()='"+str(pagemean)+"']").click()#进入第一页
#     //*[@id="xsxkapp"]/div/div[3]/div[3]/div/div[1]/div[3]/table/tbody/tr[1]/td[7]/div/span
        d = wd.find_element(By.XPATH, '//*[@id="xsxkapp"]/div/div[3]/div[3]/div/div[1]/div[3]/table/tbody')#每页课程的项目
        list = d.find_elements(By.TAG_NAME, "tr")
        num = len(list)#课程数
        result = []#保存当前页每一个课程列表的带有下标位置
        index = 1
        if num > 0:
            for i in range(num):
                result.append('//*[@id="xsxkapp"]/div/div[3]/div[3]/div/div[1]/div[3]/table/tbody/tr[' + str(index) + ']')
                index += 1

            for elem in result:
                class_name = wd.find_element(By.XPATH, elem + '/td[2]/div/div/span').text#课程名
                print(class_name)
                wd.execute_script("arguments[0].click()",
                                  wd.find_element(By.XPATH, elem + '/td[2]/div/div/span'))  # 点击
                if class_name not in has_chosen and wd.find_element(By.XPATH, elem + '/td[6]/div/div/span').text != "已满":#满足条件没选过的and 没有满and 是网课
                    wd.execute_script("arguments[0].click()",
                                      wd.find_element(By.XPATH,
                                                      elem + '/td[9]/div/button/span'))#点击选课
                    time.sleep(0.0001)
                    wd.execute_script("arguments[0].click()",
                                      wd.find_element(By.XPATH,
                                                      '/html/body/div[@aria-label="提醒"]/div/div[3]/button[2]/span'))#确认选课
                    print("sucess!!成功抢到"+class_name)
                    has_chosen.append(class_name)
                    if len(has_chosen) == 5:
                        isend1 = 1
                        isend2 = 1#退出循环的标识
                        break
        if isend1 == 1:
            break
    if isend2 == 1:
        break

time.sleep(1)
wd1 = webdriver.Chrome()
time.sleep(1000000)