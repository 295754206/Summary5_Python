# 注意字典左右两边都要加引号，右边除了数值

empty = {}

person = {
    "first_name": "Amanda",
    "last_name": "Smith",
    "age": 20
}

# 根据键获取值

first_name = person.get("first_name")

# 如果不存在会返回 None

email = person.get("email")
if (email is None):  # None用is做判断
    print("User has no email")
else:
    print("User email is " + email)

# 为获取不到的情况设置默认值

std_type = person.get("student_type", "N/A")
credit_point = person.get("credit_point", 0)

# 获取字典值或者更改值

person["first_name"] = "Mandy"
person["last_name"] = "Jones"
person["age"] = 24

# 删除键对值

del person["email"]

# 清除字典

person.clear()

# 使用范例

country = input("Enter country: ")
capital = capital_city.get(country)
if capital is None:
    print("Sorry I don't know the capital city of " + country)
else:
    print("Capital city of {0} is {1}".format(country, capital))

# 遍历键、值、键值对

spam = {
    "first_name": "Amanda",
    "last_name": "Smith",
    "age": 20
}
for v in spam.values():
    print(v)
for k in spam.keys():
    print(k)
for i in spam.items():
    print(i)
for k, v in spam.iems():
    print(k + '=' + str(v))

# 集合是可以自动去重的

a = {'a', 'b', 'a', 'c'}
b = set(a_list)

# 列表套字典

p0 = {'a', 'b', 'c'}
p1 = {'a', 'b', 'c'}
p2 = {'a', 'b', 'c'}
ls = [p0, p1, p2]
a = len(ls)  # 3

for p in ls:
    print(p)

# 字典套列表

p = {
    'name': 'some',
    'age': '18',
    'like': [
        'abc',
        'bcd'
    ]
}
print(f"{p['name']} like:")

for i in p['like']:
    print(i)
