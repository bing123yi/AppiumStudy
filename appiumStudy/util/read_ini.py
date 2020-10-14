import configparser


class ReadIni:

    def __init__(self, file_path=None):
        if file_path is None:
            self.file_path = 'D:\code\python\\appiumStudy\config\LocalElement.ini'
        else:
            self.file_path = file_path
        self.data = self.read_ini()


    def read_ini(self):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.file_path)
        return read_ini

    def get_ini_value(self, key, section=None):
        if section is None:
            section = 'default_element'
        return self.data.get(section, key)


if __name__ == '__main__':
    a = ReadIni()
    print(a.get_ini_value('test'))
