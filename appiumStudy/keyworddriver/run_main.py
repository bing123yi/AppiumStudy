from get_case_excel_data import GetCaseExcelData
from action_method import ActionMethod
from util.server import Server

class RunMain:
    def __init__(self):
        self.server = Server()
        self.server.main()
        self.case_data = GetCaseExcelData()
        self.action_method = ActionMethod()

    def run_method(self):
        lines = self.case_data.get_case_lines()
        for i in range(2, lines+1):
            handle_step = self.case_data.get_handle_step(i)
            handle_element = self.case_data.get_handle_element(i)
            handle_value = self.case_data.get_handle_value(i)
            expect_step = self.case_data.get_expect_step(i)
            expect_element = self.case_data.get_expect_element(i)
            excute_method = getattr(self.action_method, handle_step)
            if handle_element is None:
                excute_method(handle_value)
            else:
                excute_method(handle_element, handle_value)
            if expect_step is not None:
                expect_excute_method = getattr(self.action_method, expect_step)
                result = expect_excute_method(expect_element)
                if result is not None:
                    self.case_data.write_result(i, 'pass')
                else:
                    self.case_data.write_result(i, 'fail')

if __name__ == '__main__':
    run = RunMain()
    run.run_method()
