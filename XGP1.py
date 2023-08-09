from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import warnings
from selenium.common.exceptions import NoSuchElementException
import ctypes
import pyperclip

# 复制文本
def copy_text(text):
    pyperclip.copy(text)


# 设置控制台标题
def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

set_console_title("𝓢𝓬𝓻𝓲𝓹𝓽 𝓑𝔂 𝓕𝓾𝔁𝓲𝓾 modifed by Kawakaze")
warnings.filterwarnings('ignore')

# 随机生成Xbox用户名 格式为'Sa3ura + Randomchar()'
def randomUsername(length=16):
    base_Str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    random_str = ''
    for i in range(length):
        random_str += base_Str[random.randint(0, (len(base_Str) - 1))]
    return random_str


# Logo
print('''
[+]一个简单的 半 自动购买微软XGP 自动设置我的世界IGN 使用支付宝自动微软退款的脚本 如果一切正常 唯一需要手动操作的地方就是扫码绑定。
[Update Log]优化速度减少支付出现问题
[Version]当前版本 B230524 DEBUG-fork
原作者 𝓕𝓾𝔁𝓲𝓾
二次修改 白洲アズサ || Kawakaze
"Et Omina Vanitas"
[+]手动确认签约状况 减少发生错误的概率
[+]新增断点功能 位于
   1.支付宝绑定检测页面
   2.付款方式无效检测页面(一般不会触发)
   2.XboxID检测页面
''')

# 输入邮箱密码是否已经注册xbox
acc = input('Account:')
parts = acc.split("----")
Email = parts[0]
Password = parts[1]
print("W：最好是全新ms账号 登陆过Xbox或者设置过ID或付款方式的账号容易发生错误，按下回车继续")
Xbox = input("")
print("正在启动浏览器(除非控制台要求操作页面，请不要在任何时候操作浏览器的任何部分！！))")
Xbox_User = 'AzusaZi' + randomUsername(6)
IGN = 'AzusaZi' + randomUsername(6)

# 设置Edge浏览器驱动
edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = False
edge_options.add_experimental_option('useAutomationExtension', False)
edge_options.add_argument('--inprivate')

# 添加excludeSwitches参数，禁用调试信息
edge_options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])


# 创建Edge浏览器对象
driver = webdriver.Edge('msedgedriver.exe',options=edge_options)

# 打开微软账户管理页面
print('[Debugger]即将打开浏览器并自动购买......')
driver.get('https://www.xbox.com/zh-HK/xbox-game-pass#join')
time.sleep(5)
# 在页面上查找29港币的PC Game pass
print("在页面上查找29港币的PC Game pass")
join_button = driver.find_element(By.CSS_SELECTOR, "a[data-bi-source='CFQ7TTC0KGQ8']").click()
time.sleep(5)
# 输入邮箱
print('[Debugger]即将自动输入邮箱密码登录......')
input_email = driver.find_element(By.NAME,'loginfmt').send_keys(Email)
# 点击下一步
print("点击下一步")
next_button = driver.find_element(By.ID,'idSIButton9').click()
time.sleep(2)
# 输入密码

print("输入密码")
input_pwd = driver.find_element(By.NAME,'passwd').send_keys(Password)
time.sleep(1)
# 点击登录
print("点击登录")
login_button = driver.find_element(By.ID,'idSIButton9').click()
time.sleep(2)
# 点击保持登录状态
print("点击保持登录状态")
try:
  keep_login_button = driver.find_element(By.ID,'idSIButton9').click()
  time.sleep(8)
except NoSuchElementException:
   skip_button = driver.find_element(By.ID,'iShowSkip').click()
   time.sleep(5)
   keep_login_button = driver.find_element(By.ID,'idSIButton9').click()
   time.sleep(5)
   cancel_button_1 = driver.find_element(By.ID,'iCancel').click()
   time.sleep(30)
# 输入Xbox用户名
print("输入Xbox用户名")
try:
  print('[Debugger]即将自动设置Xbox用户名......')
  print("等待界面出现后 按下回车 注意:不要自己填写ID,仅检查ID是否有效，如果无效，请修改到合适的ID，但是不要点击'现在就开始吧'按钮")
  print("如果发现已经到了订阅页面/Xbox账号注册页面，请按下回车")
  b=input("")
  input_Xbox_username = driver.find_element(By.ID,'create-account-gamertag-input').send_keys(Xbox_User)
  #这个脑残 容易卡在这里 所以手动确认一下
  print("确认ID有效之后按下回车(不要操作页面！)")
  a=input(" ")
  print("你已经确认")
  print('[Debugger]Xbox用户名为:'+Xbox_User)
  time.sleep(3)
# 点击开始按钮
  print("点击开始按钮")
  start_button = driver.find_element(By.ID,'inline-continue-control').click()
  time.sleep(25)
# 点击下一步按钮
except NoSuchElementException:
  print("没有发现取名页面,点击下一步按钮，3s")
  time.sleep(3)
  next_button_2 = driver.find_element(By.XPATH,'//button[@aria-label="下一步"]').click()
  time.sleep(8)
# 添加付款方式
print('[Debugger]即将自动添加支付宝付款......')
driver.switch_to.frame('purchase-sdk-hosted-iframe')
add_payment_button = driver.find_element(By.XPATH, '//button[@class="primary--DXmYtnzQ base--kY64RzQE"]').click()
time.sleep(5)
# 选择PayPal或Alipay支付
print("选择PayPal或Alipay支付")
try:
  eWallet_button = driver.find_element(By.ID,'displayId_ewallet').click()
  time.sleep(1)
except NoSuchElementException:
  print("没有发现二维码，可能之前你已经开通过了，请确认页面位于支付宝签约二维码处，然后点击回车")
  print("如果你发现页面上面已经有一个支付宝选项 则说明这个账号已经有人绑定过支付宝了 如果确定继续，请按照如下步骤操作:")
  print("1，点击确定")
  print("2.点击新增付款方式")
  a=input("3.选择支付宝 确认页面位于支付宝签约二维码处，然后点击回车")
# 等待扫码
print('[Debugger]等待支付宝扫码...')
print("开通后按回车")
a=input("")
print("你已经手动确认,3s")
time.sleep(3)
# 点击继续
print("点击继续")
time.sleep(5)
continue_button = driver.find_element(By.ID,'pidlddc-button-alipayContinueButton').click()
time.sleep(3)
# 输入城市 & 地址
try:
  print("输入城市 & 地址")
  input_city = driver.find_element(By.ID,'city').send_keys('1')
  input_address = driver.find_element(By.ID,'address_line1').send_keys('1')
# 点击储存按钮
  print("点击储存按钮")
  save_button = driver.find_element(By.ID,'pidlddc-button-saveButton').click()
  time.sleep(12)
except NoSuchElementException:
  print("未发现设置地址的页面 按照推测 你已经到达订阅页面 这属于极端情况 说明很有可能这不是新号 如果想继续 请继续")
  pass
# 点击订阅按钮
print("手动点击订阅按钮 然后回车")
a=input(" ")
# 等待购买成功
print("等待购买成功")
time.sleep(18)
print('[Debugger]购买成功!')
# 打开官网设置ID
print('[Debugger]即将跳转官网为您自动设置ID.....')
driver.get('https://www.minecraft.net/en-us/msaprofile/mygames/editprofile')
time.sleep(10)
#点击登录按钮
home_login_button = driver.find_element(By.CSS_SELECTOR,"a[aria-label='Sign in with Microsoft account']").click()
time.sleep(13)
# 输入随机ID
input_ID = driver.find_element(By.CSS_SELECTOR,"input[name='profileName']").send_keys(IGN)
# 确认
set_ID_button = driver.find_element(By.CSS_SELECTOR,"button[aria-label='Set up your Profile Name']").click()
time.sleep(6)
print('[Debugger]ID设置成功! ID为:' + IGN)
# 打开微软退款
print('[Debugger]即将打开退款链接并自动退款......')
driver.get('https://account.microsoft.com/services/pcgamepass/cancel?fref=billing-cancel&lang=en-US')
time.sleep(20)
try:
  cancel_button = driver.find_element(By.CSS_SELECTOR,"button[aria-label='Cancel subscription']").click()
# 点击保持登录
except NoSuchElementException:
# 点击取消订阅按钮
  driver.implicitly_wait(5)
  next_button_2 = driver.find_element(By.ID,'id__0').click()
  time.sleep(25)
  cancel_button = driver.find_element(By.CSS_SELECTOR,"button[aria-label='Cancel subscription']").click()
#选择立即退款按钮
refund_button = driver.find_element(By.CSS_SELECTOR,"input[aria-label='Cancel now and get refund']").click()
#点击取消订阅按钮
cancel_button = driver.find_element(By.ID,'cancel-select-cancel').click()
time.sleep(15)
print('[Debugger]已经成功退款！')
print('账号信息:' + Email + '----' + Password + '----' + IGN)
copy_text(Email + '----' + Password + '----' + IGN)
print('已经为您复制好。')
input('按回车键退出脚本。')