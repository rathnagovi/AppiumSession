from appium import webdriver

desired_cap={
  "deviceName": "Android Emulator",
  "platformName": "Android",
  "appPackage": "com.android.calculator2",
  "appActivity": "com.android.calculator2.Calculator",
  "avd": "Govi",
  "avdLaunchTimeout": 150000

}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
driver.implicitly_wait(30)

driver.find_element_by_id("com.android.calculator2:id/digit_5").click()
driver.find_element_by_id("com.android.calculator2:id/op_add").click()
driver.find_element_by_id("com.android.calculator2:id/digit_3").click()
driver.find_element_by_id("com.android.calculator2:id/eq").click()
res=driver.find_element_by_id("com.android.calculator2:id/result").text
print(res)
if(int(res)==8):
    print("pass")
else:
    print("fail")







