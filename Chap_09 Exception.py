# 基本格式

try:

except ExceptionA as e:

except ExceptionB as e:

except ExceptionC as e:

except:  # 接受任意错误都执行

else:  # 前面所有意外都不发生才执行

finally:  # finally 表示一定会执行

# int()一个str：ValueError
# 除0错误：ZeroDivisionError
# 找不到模块错误：ModuleNotFoundError
# 未命名错误：NameError
# 列表取元素超范围错误：IndexError

# 类名不应以Error结尾

# BaseException
# Exception
# ValueError NameError ArithmeticError(ZeroDivisionError)

# Raise Error

try:
    user_input = input("Enter an integer: ")
    number = int(user_input)
    print("You have entered {0}".format(number))
except ValueError as e:
    print(e)  # e是原来错误信息输出
    print("You have entered an invalid number")  # 输出自定义错误信息

# 范例是 ValueError 和 ZeroDivisionError

try:
    user_input = input("Enter the 1st integer: ")
    number1 = int(user_input)
    number2 = int(user_input)
    quotient = number1 / number2
    print("{0} / {1} = {2}".format(number1, number2, quotient))
except ValueError as e:
    print("You have entered an invalid number")
except ZeroDivisionError as e:
    print("Invalid division - cannot divide by 0")

# try-except 的嵌套

try:
    user_input = input("Enter a positive integer: ")
    try:
        number = int(user_input)
    except:
        raise ValueError("Invalid integer format ")  # 自定义错误信息
    if (number <= 0):
        raise ValueError("Input must be a positive number ")  # if 也可以抛错
        print("You have entered {0}".format(number))
except ValueError as e:  # 这边用来接收，并指定输出格式
    print("Error: " + str(e))

# 范例：不断要求输入直到正确输入正整数

while True:
    try:
        user_input = input("Enter a positive integer: ")
        try:
            number = int(user_input)
        except:
            raise ValueError(" Invalid integer format ")
        if (number <= 0):
            raise ValueError(" Input must be a positive number ")
        print("You have entered {0}".format(number))
        break
    except ValueError as e:
        print("Error: " + str(e))


# 自定义错误类


class BadInputError(Exception):

    def __init__(self, message):
        self.message = message

try:
    print("1) Green eggs and ham")
    print("2) Red breads with jam")
    print("3) Blue salad with lamb chops")
    food_option = input("Enter your selection (1/2/3): ")
    if food_option == "1":
        food = "green eggs and ham"
    elif food_option == "2":
        food = "red breads with jam"
    elif food_option == "3":
        food = "blue salad with lamb chops"
    else:
        raise BadInputError("You have to choose 1, 2 or 3.")

    print("Drink size:")
    print("S) Small")
    print("M) Medium")
    print("L) Large")
    drink_option = input("Enter your selection (S/M/L): ")
    if drink_option == "S":
        drink = "small drink"
    elif drink_option == "M":
        drink = "medium drink"
    elif drink_option == "L":
        drink = "large drink"
    else:
        raise BadInputError("You have to choose S, M or L.")

except BadInputError as e:
    print(e.message)


# 追朔式报错

def spam():
    bacon()


def bacon():
    raise Exception("This is error info")  # Exception()这边可以直接塞错误信息


spam()

# 把错误写入文件

import traceback

try:
    raise Exception('This is the error message')
except:
    errorFile = open('error_info.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print("错误已写入文件")

# 断言：Assertion

ages = [28, 32, 97, 72]
ages.sort()
# 这边直接认定（判断）这个条件，条件符合继续，条件不符合报错右边信息
assert ages[0] < ages[-1], "The first should <= the last"

# logging 控制台输出信息
import logging

# 设置logging 输出格式
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# 开始运作
logging.debug('Start Debug')


def factorial(n):
    logging.debug("Start of fac(%s)" % n)
    total = 1
    for i in range(1, n + 1):
        total *= i
    logging.debug(f'i is {i}, total is {total}')
    logging.debug('End of fac(%s)' % n)
    return total

print(factorial(5))
logging.debug("End")
