path = r'C:\Users\lenovo\Desktop\gitskills\sunck.txt'
with open(path, 'r')as f:
    data = f.read()
    print(len(data.split()))
