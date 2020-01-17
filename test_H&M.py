from appium import webdriver
import time
from appium.webdriver.extensions.android.nativekey import AndroidKey
import pytest


class Test():
    @pytest.fixture(scope='class')

    def test_setup(self):


        self.driver = webdriver.Remote("http://localhost:4723/wd/hub",

            desired_capabilities = {
            "deviceName": "Android Emulator",
            "platformName": "Android",
            "avd": "Rathna",
            "avdLaunchTimeout": 150000,
            "appPackage": "com.hm.goe",
            "appActivity": "com.hm.goe.app.home.HomeActivity",
            "app": "Users/mycon/Downloads/com.hm.goe_2019-12-16.apk"
        })


        yield
        self.driver.close
    print("Test Completed")


def Test_login(self):
    self.driver.implicitly_wait(30)
    self.driver.find_element_by_xpath("//android.widget.TextView[@text='United States/English']").click()
    self.driver.find_element_by_id("android:id/button2").click()
    # driver.find_element_by_id("android:id/button1").click()
    self.driver.find_element_by_xpath("//android.widget.Button[1]").click()
    # driver.find_element_by_class_name("android.widget.ImageButton").click()
    time.sleep(10)
    # driver.find_element_by_xpath("//android.widget.TextView[@text='Women']").click()
    self.driver.find_element_by_xpath("//android.widget.TextView[@content-desc='Search']").click()
    self.driver.find_element_by_id("com.hm.goe:id/search_src_text").send_keys("Pants")
    self.driver.press_keycode(AndroidKey.ENTER)
