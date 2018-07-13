from pyexcel_xls import save_data
from collections import OrderedDict
import json


def TxtSaveXls(path1, path2):
    order = OrderedDict()
    with open(path1, 'r', encoding='utf-8')as f:
        all_data = json.loads(f.read())
        order.update({"numbers": all_data})
        save_data(path2, order)


if __name__ == '__main__':
    TxtSaveXls('numbers.txt', 'numbers.xls')
