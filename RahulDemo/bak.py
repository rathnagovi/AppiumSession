from appium import webdriver
import time
from appium.webdriver.extensions.android.nativekey import AndroidKey

desired_cap={
  "deviceName": "Android Emulator",
  "platformName": "Android",
  "avd": "Rathna",
  "avdLaunchTimeout": 150000,
  "appPackage": "com.hm.goe",
  "appActivity": "com.hm.goe.app.home.HomeActivity",
  "app": "Users/mycon/Downloads/com.hm.goe_2019-12-16.apk"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)

driver.find_element_by_xpath("//android.widget.TextView[@text='United States/English']").click()
driver.find_element_by_id("android:id/button2").click()
#driver.find_element_by_id("android:id/button1").click()
driver.find_element_by_xpath("//android.widget.Button[1]").click()
#driver.find_element_by_class_name("android.widget.ImageButton").click()
time.sleep(10)
#driver.find_element_by_xpath("//android.widget.TextView[@text='Women']").click()
driver.find_element_by_xpath("//android.widget.TextView[@content-desc='Search']").click()
driver.find_element_by_id("com.hm.goe:id/search_src_text").send_keys("Pants")
driver.press_keycode(AndroidKey.ENTER)