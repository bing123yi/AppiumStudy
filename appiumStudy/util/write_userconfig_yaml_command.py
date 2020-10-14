import yaml


class WriteUserconfigCommand:

    def __init__(self):
        self.yaml_path = '../config/appiumConfig.yaml'

    def read_yaml_data(self):
        """
        加载appiumConfig.yaml数据
        :return:
        """
        with open(self.yaml_path) as fr:
            data = yaml.safe_load(fr)
        return data

    def get_value_by_key_port(self, key, port):
        data = self.read_yaml_data()
        return data[key][port]

    def write_data_to_yaml(self, i, device, bp, port):
        """
        将数据写入到appiumConfig.yaml文件中
        :param data:
        :return:
        """
        data = self.join_data(i, device, bp, port)
        with open(self.yaml_path, 'a') as fr:
            yaml.dump(data, fr, default_flow_style=False)

    def join_data(self, i, device, bp, port):
        data = {
            "appium_info_" + str(i): {
                "deviceName": device,
                "bp": bp,
                "port": port
            }
        }
        return data

    def clear_data(self):
        with open(self.yaml_path, 'w') as fr:
            fr.truncate()
        fr.close()

    def get_yaml_lines(self):
        data = self.read_yaml_data()
        return len(data)


if __name__ == '__main__':
    write = WriteUserconfigCommand()
    print(write.write_data_to_yaml(1, 'device', '4831', '8501'))
