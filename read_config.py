from configparser import ConfigParser


class ReadConfig(object):
    def __init__(self, file_name):
        self.cf = ConfigParser()
        self.cf.read(file_name, encoding="utf-8")

    def get_int(self, section, option):
        """从配置文件中获取一个整数值"""
        value = self.cf.getint(section, option)
        return value

    def get_bool(self, section, option):
        """从配置文件中获取一个布尔值"""
        value = self.cf.getboolean(section, option)
        return value

    def get_float(self, section, option):
        """从配置文件中获取一个浮点值"""
        value = self.cf.getfloat(section, option)
        return value

    def get_str(self, section, option):
        """从配置文件中获取一个字符串"""
        value = self.cf.get(section, option)
        return value

    def get_data(self, section, option):
        """从配置文件中获取一个字典、元组、列表等类型的数据"""
        value = self.cf.get(section, option)
        return eval(value)


if __name__ == '__main__':
    res = ReadConfig("case.conf").get_int("CASE", "age")
    print(res)

