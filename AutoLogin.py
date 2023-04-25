from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep

# 设置无头浏览器
chrome_options = Options()
chrome_options.add_argument('--headless')

# 设置浏览器（这里使用 Chrome 作为示例）
driver = webdriver.Chrome(options=chrome_options)
#如果不用无头浏览器，可以使用下面的代码
#browser = "输出你的浏览器路径"
#driver = webdriver.Chrome(executable_path=browser)

# 打开校园网登录页面
driver.get("###########")#修改为你的校园网登入网址

# 等待页面加载完毕
#在使用无头浏览器时，等待页面加载完毕的代码没有用，所以注释掉了
#wait = WebDriverWait(driver, 3)
sleep(3)

#判断是否登入
if len(driver.find_elements(By.XPATH, "//button[contains(text(),'注销')]")) > 0:#可以通过html代码寻找登入成功的标志，这里是通过寻找”注销“按钮来判断，#通过html代码找到对应的id，可以使用快捷键ctrl+shift+c方便寻找
    print("你已经能够上网冲浪咧！")
    # 关闭浏览器
    driver.quit()

else:
    print("你还没有登入，正在为你登入中...")
    # 输入账号密码,修改为你的账号密码
    your_username="#######"##############################
    your_password="#######"##############################
    driver.find_element(By.ID, "username").send_keys(your_username)#通过html代码找到对应的id，可以使用快捷键ctrl+shift+c方便寻找，修改”username“为相对于的值
    driver.find_element(By.ID, "password").send_keys(your_password)#通过html代码找到对应的id，可以使用快捷键ctrl+shift+c方便寻找，修改”password“为相对于的值

    # 点击登录按钮
    driver.find_element(By.ID, "login-account").click()#通过html代码找到对应的id，可以使用快捷键ctrl+shift+c方便寻找，修改”login-account“为相对于的值

    # 等待连接响应（可以根据实际情况调整等待时间）
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'注销')]"))
    )#可以通过html代码寻找登入成功的标志，这里是通过寻找”注销“按钮来判断，#通过html代码找到对应的id，可以使用快捷键ctrl+shift+c方便寻找
    # 关闭浏览器
    driver.quit()
    print("嗨嗨，你已经能够上网冲浪咧！")
