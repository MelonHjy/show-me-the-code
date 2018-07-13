from pyexcel_xls import get_data
from xml.dom.minidom import Document
import json


def XlsSaveXml(path1, path2):
    data = get_data(path1)
    for key, value in data.items():
        dic = {}
        for L in value:
            num = L.pop(0)
            dic[num] = L
        text_data = json.dumps(dic, ensure_ascii=False)
        # print(text_data)
        # print(type(text_data))
        dom = Document()
        root = dom.createElement('root')
        dom.appendChild(root)
        city = dom.createElement(key)
        root.appendChild(city)
        comment = dom.createComment('\n城市信息\n')
        city.appendChild(comment)
        text = dom.createTextNode(text_data)
        city.appendChild(text)
        with open(path2, 'w', encoding='utf-8') as f:
            dom.writexml(f, newl='\n', encoding='UTF-8')


if __name__ == '__main__':
    XlsSaveXml(r'city.xls', r'city.xml')
