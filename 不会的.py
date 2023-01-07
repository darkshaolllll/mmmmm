#/////////////////////////////////////////////
# vscode使用chromedriver闪退

# 解决方案：
# 1、网上找到的基本都说是版本号的问题，多次卸载重装各个版本的chromedriver都无法解决闪退问题。
# 2、以为是以前装的插件与chromedriver产生冲突，卸载重装chrome依旧无法解决闪退问题。
# 3、以为是代码的写的有问题，复制网上大佬各种各样的代码也都无法解决闪退
# 4、在cmd中运行代码发现没有报错，这才理解到是vscode的问题。百度发现在代码后加time.sleep(）防止闪退。或者在运行时不用f5而是右键在终端中运行python文件也不会闪退。（具体的原因不太清楚，望大佬评论区指教
#/////////////////////////////////////////////


#火狐浏览器的的无头模式谷歌同样具有无头浏览器模式
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# 创建浏览器对象
options = Options()
options.add_argument("-headless")
driver = webdriver.Firefox(firefox_options=options)
# driver = webdriver.Firefox()  # # 不加 firefox_options 参数就是正常的打开一个浏览器，进行操作
driver.implicitly_wait(10)

# 访问URL
driver.get('https://www.baidu.com')
print(driver.title)  # 百度一下，你就知道
driver.quit()
#https://www.cnblogs.com/Neeo/articles/13949854.html
#################################################################################################
