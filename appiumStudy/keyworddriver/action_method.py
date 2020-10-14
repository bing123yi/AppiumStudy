from util.get_element_by_key import GetElementByKey
from base.base_driver import BaseDriver
import time


class ActionMethod:

    def __init__(self):
        driver = BaseDriver()
        self.driver = driver.android_driver(0)
        self.get_element_by_key = GetElementByKey(self.driver)

    def get_element(self, *args):
        """
        封装关键字get_element  获取元素方法
        :param args[0] : element 元素名称  通过 “:” 符号进行分割  element_name 和  section
        :return:
        """
        element_value = args[0].split(':')
        section = element_value[0]
        element_name = element_value[1]

        element = self.get_element_by_key.get_element(element_name, section)
        return element

    def input(self, *args):
        """
        封装关键字input  输入内容 方法
        :param args[0] : element_key 元素名称（对应操作元素）
        :param args[1]:  value 输入值 （对应操作值）
        :return:
        """
        element_key = args[0]
        value = args[1]
        element = self.get_element(element_key)
        if element is None:
            return element_key, "元素未找到~"
        element.send_keys(value)

    def click(self, *args):
        """
        封装关键字click 元素点击
        :param args[0] : element_key: 元素名称（对应操作元素）
        :return:
        """
        element_key = args[0]
        element = self.get_element(element_key)
        if element is None:
            return element_key, "元素未找到~"
        element.click()

    def sleep_time(self, *args):
        """
        封装关键字sleep_time 等待时间
        :param args[0] :value: 输入值 （对应操作值）
        :return:
        """
        value = args[0]
        time.sleep(value)

    def get_size(self, *args):
        """
        获取屏幕尺寸size
        :return:
        """
        window_size = self.driver.get_window_size()
        return window_size

    def swipe_left(self, *args):
        """
        向左滑动
        :return:
        """
        size = self.get_size()
        x = size['width'] * 3 / 4
        x1 = size['width'] / 4
        y = size['height'] / 2
        self.driver.swipe(x, y, x1, y)

    def swipe_right(self, *args):
        """
        向右滑动
        :return:
        """
        size = self.get_size()
        x = size['width'] / 4
        x1 = size['width'] * 3 / 4
        y = size['height'] / 2
        self.driver.swipe(x, y, x1, y)

    def swipe_up(self, *args):
        """
        向上滑动
        :return:
        """
        size = self.get_size()
        x = size['width'] / 2
        y = size['height'] * 3 / 4
        y1 = size['height'] / 4
        self.driver.swipe(x, y, x, y1)

    def swipe_down(self, *args):
        """
        向下滑动
        :return:
        """
        size = self.get_size()
        x = size['width'] / 2
        y = size['height'] / 4
        y1 = size['height'] * 3 / 4
        self.driver.swipe(x, y, x, y1)

    # def swipe_on(self, direction):
    #     if direction == 'left':
    #         self.swipe_left()
    #     elif direction == 'right':
    #         self.swipe_right()
    #     elif direction == 'up':
    #         self.swipe_up()
    #     else:
    #         self.swipe_down()
