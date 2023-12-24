import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import warnings
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import ctypes
import pyperclip
import pywinauto
from pywinauto.keyboard import send_keys
import os


# 复制文本
def copy_text(text):
    pyperclip.copy(text)


# 设置控制台标题
def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)


set_console_title("autoxgp by huaji")
warnings.filterwarnings('ignore')


# 随机生成Xbox用户名 格式为'Sa3ura + Randomchar()'
def randomUsername(length=16):
    base_Str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    random_str = ''
    for i in range(length):
        random_str += base_Str[random.randint(0, (len(base_Str) - 1))]
    return random_str


def purchasecheck():
    try:
        success = driver.find_element(By.XPATH,
                                      '/html/body/reach-portal/div[3]/div/div/div/div/div/div/div/div/div/div/div[2]/div[3]/a')
        success = int(success)
        if success == '<selenium.webdriver.remote.webelement.WebElement (session="9a245c8242c7806aae13821738d81698", element="23F5752506E09117C6B47DABC432C962_element_221")>':
            s = 1
        else:
            s = 2
    except NoSuchElementException:
        print('等待中......')
        s = 2
        return False


# Logo
print('''
[+]一个简单的半自动购买微软XGP 自动设置我的世界IGN，自动设置皮肤 使用支付宝自动微软退款的脚本 如果一切正常 唯一需要手动操作的地方就是扫码绑定。
[Version]当前版本 A20231111
[+]脑瘫Xpath，已修复,必须为新号
新增自动选择皮肤（查看readme）
W:梯子必须好，不然掉登陆
''')
# 输入邮箱密码是否已经注册xbox

acc = input('Account----Password:')
parts = acc.split("----")
Email = parts[0]
Password = parts[1]
print("必须为新号！必须为新号！必须为新号！必须为新号！必须为新号！必须为新号！必须为新号！浏览器似乎得全屏才能正常使用")
print("正在启动浏览器(除非控制台要求操作页面，请不要在任何时候操作浏览器的任何部分！！))")
Xbox_User = 'AzusaZi' + randomUsername(6)
IGN = 'A' + randomUsername(2) + 'D' + randomUsername(2)

# 设置Edge浏览器驱动
edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = False
edge_options.add_experimental_option('useAutomationExtension', False)
edge_options.add_argument('--inprivate')

# 添加excludeSwitches参数，禁用调试信息
edge_options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])

# 创建Edge浏览器对象
driver = webdriver.Edge('msedgedriver.exe', options=edge_options)


#询问用户是否已经设置XboxID
#          废弃        #

# 打开微软账户管理页面
print('[Debugger]即将打开浏览器并自动购买......')
driver.get('https://www.xbox.com/zh-HK/xbox-game-pass#join')
# 在页面上查找29港币的PC Game pass
print("在页面上查找29港币的PC Game pass")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "a[data-xbbigid='CFQ7TTC0KGQ8']").click()
WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.NAME, 'loginfmt'))).send_keys(Email)
# 输入邮箱
print('[Debugger]即将自动输入邮箱密码登录......')
# 点击下一步
print("点击下一步")
next_button = driver.find_element(By.ID, 'idSIButton9').click()
time.sleep(2)
# 输入密码
print("输入密码")
WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.NAME, 'passwd'))).send_keys(Password)
print("点击登录")
WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.ID, 'idSIButton9'))).click()
# 点击保持登录状态
print("点击保持登录状态")
WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.ID, 'idSIButton9'))).click()
# 输入Xbox用户名
try:
    print("输入Xbox用户名")
    print('[Debugger]即将自动设置Xbox用户名......（15sec）')
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, 'create-account-gamertag-input'))).send_keys(Xbox_User)
    print("确认ID有效之后按下回车(不要操作页面！)")
    b = input("")
    # 这个脑残 容易卡在这里 所以手动确认一下
    print("你已经确认")
    # 点击开始按钮
    print("点击开始按钮...8sec")
    WebDriverWait(driver, 4).until(EC.visibility_of_element_located((By.ID, 'inline-continue-control'))).click()
    time.sleep(4)
    print("正在跳过按钮")
    driver.get('https://www.xbox.com/zh-HK/xbox-game-pass?launchStore=CFQ7TTC0KGQ8#join')
    time.sleep(4)
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//button[@aria-label="下一步"]'))).click()
    # 点击下一步按钮
except TimeoutException:
    print("没有发现取名页面,点击下一步按钮")
    WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, '//button[@aria-label="下一步"]'))).click()
    time.sleep(8)
    # 添加付款方式
print('[Debugger]即将自动添加支付宝付款......')
driver.switch_to.frame('purchase-sdk-hosted-iframe')
WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.XPATH, '//button[@class="primary--DXmYtnzQ base--kY64RzQE"]'))).click()
time.sleep(2)
# 选择PayPal或Alipay支付
print("选择PayPal或Alipay支付")

time.sleep(5)
try:
    #driver.find_element(By.XPATH, '/html/body/section/div[1]/div/div/div/div/div[2]/div/div[4]/button[2]').click()
    WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="displayId_ewallet"]'))).click()
    WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="displayId_ewallet_alipay_billing_agreement"]'))).click()
    try:
        print("填写姓名")
        # 尝试填写姓名
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH,"/html/body/section/div[1]/div/div/div/div/div[2]/div/section/div[2]/div[1]/input"))).send_keys(randomUsername(5))
        WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH,"/html/body/section/div[1]/div/div/div/div/div[2]/div/section/div[2]/div[2]/input"))).send_keys(randomUsername(5))
        WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/section/div[1]/div/div/div/div/div[2]/div/section/div[3]/input[2]"))).click()
        time.sleep(4)
    except NoSuchElementException:
        print("未发现姓名填写页面，跳过")
except NoSuchElementException:
    print("没有发现二维码，可能之前你已经开通过了，请确认页面位于支付宝签约二维码处，然后点击回车")
    print("如果你发现页面上面已经有一个支付宝选项 则说明这个账号已经有人绑定过支付宝了 如果确定继续，请按照如下步骤操作:")
    print("1，点击确定")
    print("2.点击新增付款方式")
    a = input("3.选择支付宝 确认页面位于支付宝签约二维码处，然后点击回车")
# 等待扫码
WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="pidlddc-button-saveNextButton"]'))).click()
print('[Debugger]等待支付宝扫码...')
print("开通后按回车")
a = input("")
print("你已经手动确认,3s")
# 点击继续
print("点击继续")
continue_button = driver.find_element(By.ID, 'pidlddc-button-alipayContinueButton').click()
time.sleep(3)
# 输入城市 & 地址
try:
    print("输入城市 & 地址")
    WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.ID, 'city'))).send_keys('1')
    WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.ID, 'address_line1'))).send_keys('1')
    # 点击储存按钮
    print("点击储存按钮")
    save_button = driver.find_element(By.ID, 'pidlddc-button-saveButton').click()
    time.sleep(12)
except NoSuchElementException:
    print("未发现设置地址的页面 按照推测 你已经到达订阅页面 这属于极端情况 说明很有可能这不是新号 如果想继续 请继续")
    pass
# 点击订阅按钮
print("点击订阅按钮")
WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.XPATH, "/html/body/section/div[1]/div/div/div/div/div[2]/div/div[4]/button[2]"))).click()
# 等待购买成功
print("等待购买成功")
time.sleep(18)
'''while s == 1:
        pass
    else:
        print("等待购买结果中....")'''
print('[Debugger]购买成功!')
# 打开官网设置ID
print('[Debugger]即将跳转官网为您自动设置ID.....')
driver.get('https://www.minecraft.net/en-us/msaprofile/mygames/editprofile')
time.sleep(10)
# 点击登录按钮
WebDriverWait(driver, 2000).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#LoginAnimation_Bee > div.container > div > div > section > div:nth-child(3) > div > div.login-form-view__first-container.p-4.d-flex.flex-column.justify-content-between > div:nth-child(1) > div > a"))).click()
WebDriverWait(driver, 2000).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='profileName']"))).send_keys('Genshin_' + IGN)
# 输入随机ID
# 确认
try:
    WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label='Set up your Profile Name']"))).click()
except NoSuchElementException:
    print('按钮不可点击 稍等....4sec')
    time.sleep(4)
    WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label='Set up your Profile Name']"))).click()
time.sleep(6)
print('[Debugger]ID设置成功! ID为:' + 'Genshin_' + IGN)
#设置皮肤
print('正在设置皮肤')

driver.get('https://www.minecraft.net/en-us/msaprofile/mygames/editskin')
driver.maximize_window()
time.sleep(5)
WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/div[4]/div[1]/div/div/main/section/div/div/section[1]/div[2]/div/div[2]/div[2]/div/label"))).click()
time.sleep(3)
WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/div[4]/div[1]/div/div/main/section/div/div/section[2]/div[2]/div/div[2]/div[2]/button"))).click()
#使用pywinauto来选择文件
time.sleep(2)
app = pywinauto.Desktop()
#选择文件上传的窗口
dlg = app["打开"]

#选择文件地址输入框，点击激活
dlg["Toolbar3"].click()
#键盘输入上传文件的路径
send_keys("C:\\Users\\leiyu\\Desktop\\新建文件夹2")
time.sleep(2)
#键盘输入回车，打开该路径
send_keys("{VK_RETURN}")
time.sleep(1)

#选中文件名输入框，输入文件名
dlg["文件名(&N):Edit"].type_keys("3b83842a32159a37.png")
time.sleep(1)

#点击打开
dlg["打开(&O)"].click()
time.sleep(1)
#上传
WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/div[4]/div[1]/div/div/main/section/div/div/section[2]/div[2]/div/div[2]/div/button[1]"))).click()
time.sleep(1)


print('设置完成')
# 打开微软退款
print('[Debugger]即将打开退款链接并自动退款......')
driver.get('https://account.microsoft.com/services/pcgamepass/cancel?fref=billing-cancel&lang=en-US')
time.sleep(20)
try:
    WebDriverWait(driver, 2000).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label='Cancel subscription']"))).click()
# 点击保持登录
except NoSuchElementException:
    # 点击取消订阅按钮
    driver.implicitly_wait(5)
    WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.ID, 'id__0'))).click()
    WebDriverWait(driver, 2000).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label='Cancel subscription']"))).click()
# 选择立即退款按钮
refund_button = driver.find_element(By.CSS_SELECTOR, "input[aria-label='Cancel now and get refund']").click()
# 点击取消订阅按钮
cancel_button = driver.find_element(By.ID, 'cancel-select-cancel').click()
time.sleep(15)
print('[Debugger]已经成功退款！')
print('正在写入文档')
input('按回车键退出脚本。')
with open("accounts.txt", "a") as f:
    f.write(f"{Email}----{Password}----{'Genshin_' + IGN}\n")
