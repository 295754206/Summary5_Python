# 输出 [0,10): 0-9

for i in range(0, 10):
    print(i)

# 指定输出某个数的1-10的循环乘法

number_input = input("Enter a number: ")
number = int(number_input)

for i in range(1, 10):
    print("{0} x {1} = {2}".format(i, number, number * i))

# Friend of 10 table

for i in range(0, 11):
    print("{0:>2} + {1:>2} = {2:>2}".format(i, 10 - i, 10))

# 输出 0, 1, ... 10. 这种序列

for i in range(0, 11):
    if (i < 10):
        trailing = ", "
    else:
        trailing = "."
        print(i, end="")
    print(trailing, end="")

# 累加1-10：

result = 0
for i in range(1, 11):
    result = result + i
    print("The sum of 1 to 10 is {0}".format(result))

# 输出：
# 2 1
# 4 3 2 1
# 6 5 4 3 2 1
# 8 7 6 5 4 3 2 1
# 10 9 8 7 6 5 4 3 2 1

for i in range(1, 6):
    start_number = 2 * i
    for j in range(0, start_number):
        number = start_number - j
        print(number, end=" ")
    print()

# break 跳出循环

# 字串大小写

name = "John Smith"
name_uppercase = name.upper()
print(name_uppercase)
name = "John Smith"
name_lowercase = name.lower()
print(name_lowercase)

# 查找字子串

name = "Alexandra"
index = name.find("exa")
print(index)

# 字串长度len()

greeting = "Hi there!"
greeting_length = len(greeting)

# 截取字串

sentence = "Python is cool!"
sub_sentence1 = sentence[1:4]  # "yth" 1-4不包括4
sub_sentence2 = sentence[1:]  # "ython is cool!" 1-最后包括1
Function
sub_sentence3 = sentence[:4]  # "Pyth" 4之前不包括4

# 输出字串每个字符

greeting = "Hi there!"

for i in range(0, len(greeting)):
    letter = greeting[i]
    print(letter)

# 替换部分字符生成密码

username = "SomeString"
password = ""

for i in range(0, len(username)):
    letter = username[i]
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
    password = password + password_letter

# 计算输入的奇数偶数个数

even_count = 0
odd_count = 0

while True:
    user_input = input("Enter an integer (or q to quit): ")
    if (user_input == "q"):
        break
    number = int(user_input)
    if (number % 2 == 0):
        even_count += 1
    else:
        odd_count += 1
    print("You have entered {0} even numbers".format(even_count))
    print("You have entered {0} odd numbers".format(odd_count))
