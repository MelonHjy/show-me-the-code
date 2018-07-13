from pyexcel_xls import save_data
from collections import OrderedDict
import json


def TxtSaveXls(path1, path2):
    order = OrderedDict()
    sheet = []
    with open(path1, 'r',encoding='utf-8')as f:
        all_data = json.loads(f.read())
        for key, value in all_data.items():
            sheet.append([key, value])
        order.update({"city": sheet})
        save_data(path2, order)


if __name__ == '__main__':
    TxtSaveXls('city.txt', 'city.xls')