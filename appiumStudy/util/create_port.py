from dos_cmd import DosCmd


class CreatePort:

    def __init__(self):
        self.dos = DosCmd()

    def port_is_used(self, port_num):
        """
        判断端口号是否被占用
        :param port_num： 端口号
        :return:
        """
        flag = None
        command = 'netstat -ano | findstr ' + str(port_num)
        result = self.dos.excute_cmd_result(command)
        if len(result) > 0:
            flag = True
        else:
            flag = False
        return flag

    def create_port_list(self, start_port, device_list):
        """
        生成可用的端口号列表
        :param start_port:  开始端口号
        :param device_list: 设备列表
        :return:
        """
        if device_list == None:
            print('设备列表为空，无法生成端口号')
            return None
        else:
            port_list = []
            while len(port_list) != len(device_list):
                if not self.port_is_used(start_port):
                    port_list.append(start_port)
                start_port = int(start_port) + 1
            return port_list


if __name__ == '__main__':
    port = CreatePort()
    print(port.create_port_list(4723, ['sdfeww', 'sfd223']))
