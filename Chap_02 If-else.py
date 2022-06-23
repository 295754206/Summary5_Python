# 输入选择的一个范例

print("Choose a language: (I)talian (W)elsh (Z)ulu")
language_option = input("Enter language selection: ")
if (language_option == "I"):
    print("Ciao mondo.")
    print("Come stai?")
elif (language_option == "W"):
    print("Helo Byd.")
    print("Sut wyt ti?")
elif (language_option == "Z"):
    print("Sawubona Mhlaba.")
    print("Unjani?")
else:
    print("Hello World.")
    print("How are you?")

# 范例选择条件，注意双等号

if ((age > 40) and (student_type == “Domestic”)):

# and or not

if (not (number1 == 1000)):

# 常见输入方式：

item_input = int(input("Enter the quantity: "))
