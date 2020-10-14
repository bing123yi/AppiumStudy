from read_ini import ReadIni


class GetElementByKey:

    def __init__(self, driver):
        self.read_ini = ReadIni()
        self.driver = driver

    # 根据传入的type 返回元素定位的方法名称
    def get_find_element_fuc(self, find_type):
        if find_type == 'id':
            return self.driver.find_elements_by_id
        elif find_type == 'class':
            return self.driver.find_elements_by_class_name
        elif find_type == 'xpath':
            return self.driver.find_elements_by_xpath

    # 根据元素名称从ini文件中读取对应的value 然后调用driver直接获取返回元素信息
    def get_element(self, element_name, section=None):
        ini_value = self.read_ini.get_ini_value(element_name, section)
        split_ini_value = ini_value.split('>')
        # 配置文件ini 用>分隔调用的type及相应的值
        if len(split_ini_value) >= 2:
            find_type = split_ini_value[0]
            find_key = split_ini_value[1]
            try:
                element_value = self.get_find_element_fuc(find_type)(find_key)
            except:
                element_value = None
            if len(split_ini_value) == 3:
                index = int(split_ini_value[2])
                element_value = element_value[index]
            return element_value
        else:
            return None


if __name__ == '__main__':
    a = GetElementByKey()
    print(a.get_element('test'))
    print(a.get_element('nokey'))
