# 输出变量类型

print(type(first_name))

# 变量相乘

silly = "frog" * 7

# 输入

var = input("请输入")

# Python 不能把字串直接加数字

var = var + str(123)

# 转义字符串

print("Thursday July 30 at 7.15pm: \"Inside Out\"")

# \t是tab, \n是回车, print()自己本身就有一个回车
# 字串格式化，后面可以是字串可以是 数字、字串

print("Hi {0} {1}!".format(fname, lname))
print("{1} {2} is {0} years old".format(20, fname, lname))

# 字串对齐

print("{0:<15}{1:<10}{2:^25}{3:>15}".format("Element", "Symbol", "Atomic number", "Atomic weight)")

# /是除法，输出是精确数值的小数

10 / 2 = 5.0
10 / 4 = 2.5
10 / 2.0 = 5.0
10.0 / 1.2 = 8.3333

# //是整数除法，根据输入是否是浮点数决定输出格式，输出一定是整数输出

10 // 2 = 5
10 // 4 = 2
10 // 2.0 = 5.0
10.0 // 1.2 = 8.0

# 取余是%，找的是最后一个正整数
# 2的幂次方

2 ** 2
