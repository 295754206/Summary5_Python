# 文件mode有：r、w(已经有的会被覆盖)、a(追加)、r+(读和写)

silly_file_path = "put/the/file/path/here/silly.txt"

# 写

with open(silly_file_path, "w") as silly_file:
    # f.write()函数
    silly_file.write("Hi! ")
    silly_file.write("I am Sam.\n")
    silly_file.write("Would you like green egg and ham?\n")

user_input = input("Enter a number to generate times table: ")
number = int(user_input)
file_path = input("Enter output file path: ")
with open(file_path, "w") as timestable_file:
    for i in range(1, 10):
        timestable_file.write("{0} x {1} = {2}\n".format(number, i, number * i))

# 读

with open(text_file_path) as silly_file:
    while True:
        line = silly_file.readline()
        if (line == ""):
            break
        print(line)

with open(text_file_path) as silly_file:
    for line in silly_file:
        print(line)

# CSV 格式

# stn,first_name,last_name
# 1111,John,Smith
# 2222,Lee,May
# 3333,Ye,Zhang

import csv

student_file_path = " put/the/file/path/here/student .csv"

with open(student_file_path, "w") as student_file:
    field_name_list = ["stn", "first_name", "last_name"]
    # 写dict的写法，先定义一个writer = csv.DictWriter(文件名，列名字段名一个列表)
    # x = csv.DictWriter(f_name,field_name)
    writer = csv.DictWriter(student_file, fieldnames=field_name_list)
    # 启动：先写入header
    writer.writeheader()
    # 再以 writerow 写入字典
    writer.writerow({"stn": "1111", "first_name": "John", "last_name": "Smith"})
    writer.writerow({"stn": "2222", "first_name": "Lee", "last_name": "May"})
    writer.writerow({"stn": "3333", "first_name": "Ye", "last_name": "Zhang"})

# 获取的是每个字典，读也是按照每个字典来读的

import csv

student_file_path = " put/the/file/path/here/student.csv"

with open(student_file_path) as student_file:
    # 先是读取文件，这边是直接读取了整个文件
    x = csv.DictReader(f)
    reader = csv.DictReader(student_file)
    for row in reader:  # 用get的方式
        student_number = row.get("stn")
    fname = row.get("first_name")
    lname = row.get("last_name")
    print("{0:<10}{1:<10}{2:<10}".format(student_number, fname, lname))

# JSON 格式

# json.dump() 导入列表
# json.dump(x,f) 里面两个位置不要搞错！

import json

numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

# json.load() 读取列表

with open(filename) as f:
    numbers = json.load(f)

print(numbers)
