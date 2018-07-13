from pyexcel_xls import save_data
from collections import OrderedDict
import json


def TxtSaveXsl(path1, path2):
    order = OrderedDict()
    sheet = []
    with open(path1, 'r', encoding='utf-8')as f:
        data = json.loads(f.read())
        for key, value in data.items():
            value.insert(0, key)
            sheet.append(value)
        order.update({'students': sheet})
        save_data(path2, order)


if __name__ == '__main__':
    TxtSaveXsl('student.txt', 'student.xls')
