# 两种遍历列表方式

for i in range(0, len(animal_list)):
    print(animal_list[i])

for animal in animal_list:
    print(animal)

# .append()尾加到列表

animal_list.append("kangaroo")
animal_list.append("emu")

# .insert()插入

animal_list.insert(1, "emu")  # 1号位，0开始

# del 删除某元素

del subject_list[1]

# .remove()按值删除第一个出现的数，没有的话会报错

random_numbers = [3, 12, 4, 5, 4, 3, 2, 6, 12]
random_numbers.remove(4)

# .index() 按值找最先出现的index

four_index = random_numbers.index(4)  # 找第一个数值4的出现位置

# .count() 计算列表中数值的出现次数

four_count = random_numbers.count(4)

# sorted() 返回一个排序后的新列表，原列表不变

sorted_numbers = sorted(random_numbers)

# .sort() 是列表内部自己的函数，对自己做了修改排序

random_numbers.sort()

# .reverse() 反转列表

random_numbers.reverse()

# .clear() 清空列表所有元素

random_numbers.clear()

# 列表可以直接相加

list12 = list1 + list2

# 列表也可以乘

list3 = [9, 8]
list4 = list3 * 3

# 截取列表/列表切片注意 这里不包含4

list1 = random_numbers[1:4]

# 列表可换元素，元组不可换元素

animal_tuple = ("dog", "cat", "frog")
animal_tuple[0] = "elephant"  # ERROR

# .title() 是字串首字母大写
# 元组不可变，只能全体重置，d="12"字串也是不可局部调出来变

d = (1, 2)
d[0] = 3  # error
d = (3, 2)  # OK

# 在 b = a 中 b与a 不是同一个Id
# 但是列表 等同是 引用同一个id的
# 即使事先声名，也一样应用同一个
# 使用.copy()可以新建一个列表

a = [1, 2, 3]
b = []
b = a
b[1] = 4
print(a)  # [1,4,3]
c = a.copy()
c[1] = 2
print(a)  # a不受影响
