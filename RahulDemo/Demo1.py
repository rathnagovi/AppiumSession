from appium import webdriver

desired_cap={
  "deviceName": "Android Emulator",
  "platformName": "Android",
  "appPackage": "io.appium.android.apis",
  "appActivity": "io.appium.android.apis.ApiDemos",
  "avd": "Govi",
  "avdLaunchTimeout": 150000,
  "app" : "Users/mycon/Downloads/ApiDemos-debug.apk"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
driver.implicitly_wait(30)

driver.find_element_by_xpath("//android.widget.TextView[@content-desc='Preference']").click()
#driver.find_element_by_xpath("//android.widget.TextView[@content-desc=‘3.Preference dependencies’]").click()

driver.find_element_by_xpath("//android.widget.TextView[3]").click()
driver.find_element_by_id("android:id/checkbox").click()
ele=driver.find_elements_by_class_name("android.widget.LinearLayout").__getitem__(2).click()



driver.find_element_by_class_name("android.widget.EditText").send_keys("hello")
ele1=driver.find_elements_by_class_name("android.widget.Button").__getitem__(1).click()
