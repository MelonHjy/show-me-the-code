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
        print(text_data)
        print(type(text_data))
        dom = Document()
        root = dom.createElement('root')
        dom.appendChild(root)
        stu = dom.createElement(key)
        root.appendChild(stu)
        comment = dom.createComment('\n学生信息表\n"id":[名字,数学,语文,英文]\n')
        stu.appendChild(comment)
        text = dom.createTextNode(text_data)
        stu.appendChild(text)
        with open(path2, 'w', encoding='utf-8') as f:
            dom.writexml(f, newl='\n', encoding='UTF-8')


if __name__ == '__main__':
    XlsSaveXml(r'student.xls', r'student.xml')
