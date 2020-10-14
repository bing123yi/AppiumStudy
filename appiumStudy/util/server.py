from dos_cmd import DosCmd
from create_port import CreatePort
import threading
from write_userconfig_yaml_command import WriteUserconfigCommand
import time


class Server:

    def __init__(self):
        self.dos = DosCmd()
        self.port = CreatePort()
        self.write_yaml = WriteUserconfigCommand()
        self.device_list = self.get_devices()
        self.start_list = self.start_appium_command_list()

    def get_devices(self):
        """
        获取设备信息
        :return:
        """
        command = 'adb devices'
        result_list = self.dos.excute_cmd_result(command)
        # print(result_list)
        devices_list = []
        if len(result_list) > 1:
            for i in result_list:
                if '\tdevice' in i:
                    devices_info = i.split('\tdevice')
                    devices_list.append(devices_info[0])
            return devices_list
        else:
            return None

    def create_port(self, start_port):
        """
        生成端口号列表
        :param start_port:
        :return:
        """
        port = CreatePort()
        port_list = port.create_port_list(start_port, self.device_list)
        return port_list

    def start_appium_command_list(self):
        # appium -p 4700 -bp 4701 -U 4f368950
        """
        生成启动appium服务的命令列表集合
        :return:
        """
        # 先清空掉yaml文件 然后再写入
        self.write_yaml.clear_data()
        command_list = []
        appium_port_list = self.create_port(4700)
        bootstrap_port_list = self.create_port(4900)
        if self.device_list is not None:
            for i in range(len(self.device_list)):
                command = 'appium -p ' + str(appium_port_list[i]) + ' -bp ' + str(
                    bootstrap_port_list[i]) + ' -U ' + str(self.device_list[i]) + ' --no-reset --session-override --log D:/code/log/test01.log --local-timezone '
                command_list.append(command)
                self.write_yaml.write_data_to_yaml(i, self.device_list[i], bootstrap_port_list[i], appium_port_list[i])
        return command_list

    def start_appium_server(self, i):
        """
        通过启动命令集合 执行单个启动服务命令
        :param i:
        :return:
        """
        self.dos.excute_cmd(self.start_list[i])

    def kill_appium_server(self):
        find_command = 'tasklist | find "node.exe"'
        server_list = self.dos.excute_cmd_result(find_command)
        if len(server_list) > 1 :
            kill_command = 'taskkill -F -PID node.exe'
            self.dos.excute_cmd(kill_command)


    def main(self):
        """
        使用多线程运行启动设备服务
        :return:
        """

        # 先把当前的进程全部kill掉
        self.kill_appium_server()
        # 多线程开始启动服务
        for i in range(len(self.device_list)):
            appium_start = threading.Thread(target=self.start_appium_server, args=(i,))
            appium_start.start()
            time.sleep(10)


if __name__ == '__main__':
    server = Server()
    print(server.main())
