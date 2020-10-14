from util.opera_excel import OperaExcel


class GetCaseExcelData:
    def __init__(self):
        self.opera_excel = OperaExcel()

    def get_case_lines(self):
        """
        获取case的行数
        :return:
        """
        return self.opera_excel.max_row

    def get_handle_step(self, row):
        """
        获取case表中 操作步骤一列中的 操作方法名称
        :param row:
        :return:
        """
        method_name = self.opera_excel.get_value(row, 4)
        return method_name

    def get_handle_element(self, row):
        """
        获取case表中 操作元素一列中的 元素名称
        :param row:
        :return:
        """
        element = self.opera_excel.get_value(row, 5)
        if element == '':
            element = None
        return element

    def get_handle_value(self, row):
        """
        获取case表中 操作值一列中的 操作值
        :param row:
        :return:
        """
        value = self.opera_excel.get_value(row, 6)
        if value == '':
            value = None
        return value

    def get_expect_step(self, row):
        """
        获取case表中 预期结果操作步骤一列中的 操作方法名称
        :param row:
        :return:
        """
        method_name = self.opera_excel.get_value(row, 7)
        if method_name == '':
            method_name = None
        return method_name

    def get_expect_element(self, row):
        """
        获取case表中 预期结果操作步骤一列中的 操作方法名称
        :param row:
        :return:
        """
        element = self.opera_excel.get_value(row, 8)
        if element == '':
            element = None
        return element

    def get_is_run(self, row):
        """
        获取case表中 是否运行一列中的 yes/no
        :param row:
        :return:
        """
        is_run = self.opera_excel.get_value(row, 10)
        if is_run == 'yes':
            return True
        else:
            return False

    def write_result(self, row, value):
        """
        将结果会写到case表中 实际运行结果一列
        :param row:
        :return:
        """
        self.opera_excel.write_excel(row, 9, value)