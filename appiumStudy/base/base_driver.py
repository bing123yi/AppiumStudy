from appium import webdriver
import time
from util.write_userconfig_yaml_command import WriteUserconfigCommand

class BaseDriver:

    def __init__(self):
        self.write_yaml = WriteUserconfigCommand()

    def android_driver(self, i):

        deviceName = self.write_yaml.get_value_by_key_port('appium_info_' + str(i), 'deviceName')
        port = self.write_yaml.get_value_by_key_port('appium_info_' + str(i), 'port')
        capabilities = {
            'platformName': 'Android',
            'devicesName': deviceName,
            'automationName': 'UiAutomator2',
            'appPackage': 'com.xunmeng.pinduoduo',
            'appActivity': 'com.xunmeng.pinduoduo.ui.activity.MainFrameActivity',
            # 'app': "D:\\code\\apk\\pdd.apk",
            'noSign': True,
            'noReset': True,

        }
        driver = webdriver.Remote("http://localhost:" + str(port) + "/wd/hub", capabilities)
        time.sleep(10)
        return driver

    def ios_driver(self):
        pass

    def get_driver(self):
        pass
