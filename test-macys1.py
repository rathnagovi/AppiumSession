from appium import webdriver
from  time import sleep
from appium.webdriver.extensions.android.nativekey import AndroidKey
import pytest


class TestLogin():
    @pytest.fixture(scope="class")

    def setup(self):


        self.driver = webdriver.Remote("http://localhost:4723/wd/hub",
                                       #self.driver.implicitly_wait(30)

                        desired_capabilities = {
                        "deviceName": "Android Emulator",
                        "platformName": "Android",
                        "avd": "Rathna",
                        "avdLaunchTimeout": 150000,
                        "appPackage": "com.macys.hq2019",
                        "appActivity": "com.expectare.p865.MainActivity ",
                        })

        yield
        self.driver.close

    def test_login(self):
        self.driver.implicitly_wait(30)

        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Agree']").click()
        sleep(10)

            # driver.find_element_by_xpath("//android.widget.TextView[0]").click()
        self.driver.find_elements_by_class_name("android.widget.TextView").__getitem__(0).click()

        self.driver.find_element_by_xpath("//android.widget.TextView [@text='Search']").click()
            # driver.find_element_by_xpath("//android.widget.TextView [@text='Overview']").click()

        searchBox = self.driver.find_element_by_class_name("android.widget.EditText").send_keys("Pots and pans")


            # from appium.webdriver.extensions.android.nativekey import AndroidKey
            # sending 'Home' key event
        self.driver.press_keycode(AndroidKey.ENTER)
            # driver.keyevent(66)
            # time.sleep(15)