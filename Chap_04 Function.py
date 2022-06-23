# return 返回多个值

def ask_name():
    first_name = "Finley"
    last_name = "Fish"
    return first_name, last_name


first_name, last_name = ask_name()


# int()别忘记加了

def ask_input():
    word = input("Enter a word: ")
    user_input = input("Enter expand factor: ")
    multiplicity = int(user_input)  # int()别忘记加了
    return word, multiplicity


# 扩展字符串

def expand(word, multiplicity):
    result = ""
    for i in range(0, len(word)):
        letter = word[i]
        letter_multiply = letter * multiplicity
    result = result + letter_multiply
    return result


# 替换部分字串生成密码

def generate_password(username):
    password = ""
    for i in range(0, len(username)):
        username_letter = username[i]
        password_letter = transform_character(username_letter)  # 这边用到另一个函数
    password = password + password_letter
    return password


def transform_character(letter):
    if (letter == "i") or (letter == "I"):
        password_letter = "1"
    elif (letter == "r") or (letter == "R"):
        password_letter = "7"
    elif (letter == "s") or (letter == "S"):
        password_letter = "5"
    elif (letter == "z") or (letter == "Z"):
        password_letter = "2"
    else:
        password_letter = letter
    return password_letter


# 设置默认参数

def welcome(name, greeting="Hi"):  # 这边设置
    print("{0} {1}!".format(greeting, name))
    welcome("John", "Hello")
    welcome("Mary", greeting="It is nice to meet you")  # 这边指定参数名来做
    welcome("Paul")


# Recursive functions: 递归函数

# factorial(n) = n x factorial(n-1)

# 输出1-9的阶乘

def factorial(n):
    if (n == 1):
        return 1
    else:
        return n * factorial(n - 1)


for i in range(1, 10):
    print("{0}! = {1}".format(i, factorial(i)))

# 四舍五入函数：round

number = 28.30188679245283
rounded_number = round(number)  # 保留整数，四舍五入
rounded_number = round(number, 1)  # 保留1位小数，四舍五入
rounded_number = round(number, 2)

# max(), min() 函数既可以接受 几个直接放进来的元素，也可以接受 列表和集合

min_num = min(num1, num2, num3)

# 输出10个 1-6 之间的随机整数

import random

for i in range(0, 10):
    random_number = random.randint(1, 6)  # 这里是包含1和6的
    print("Dice result: {0}".format(random_number))
