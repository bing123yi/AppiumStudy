import os


class DosCmd:

    def excute_cmd_result(self, command):
        result = os.popen(command).readlines()
        result_list = [x.strip() for x in result if x.strip() != '']
        return result_list

    def excute_cmd(self, command):
        os.system(command)


if __name__ == '__main__':
    doscmd = DosCmd()
    print(doscmd.excute_cmd_result('adb devices'))
