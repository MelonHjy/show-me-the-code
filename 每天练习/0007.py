import os

all_filepath = []
def allpath(path):
    dir_list = os.listdir(path)
    try:
        dir_list.remove('.idea')
        dir_list.remove('__pycache__')
        dir_list.remove('venv')
    except :
        pass
    finally:
        for d in dir_list:
            new_path = os.path.join(path, d)
            if os.path.isdir(new_path):
                allpath(new_path)
            if os.path.isfile(new_path):
                all_filepath.append(new_path)


def countCode(list):
    num = 0
    blank_num = 0
    note_num = 0
    for path in list:
        with open(path, 'rb') as f:
            for line in f.readlines():
                if line.startswith(b'\n'):
                    blank_num += 1
                elif line.startswith(b'#'):
                    note_num += 1
                else:
                    num += 1
    return print('num = %s\nblank = %s\nnote = %s' % (num,blank_num,note_num))


path = r'C:\Users\lenovo\PycharmProjects\aab'
allpath(path)
countCode(all_filepath)
