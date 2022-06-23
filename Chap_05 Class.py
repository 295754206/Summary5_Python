# Instance attribute: data belongs to individual object instance.
# Class attribute: data that is common to all objects.
# (Some classes do not have any class attributes.)

class Student:
    # 类属性
    email_domain = "solla.sollew.edu"
    student_dir = "/user/student"

    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name


# Instance method: Deal with a particular individual object instance
# Static / Class method:
# 1. Do NOT deal with individual object instance
# 2. Common to all object instances
# instance method can be invoked from an object
# Use class name to call static method:

staff2.update_employment_type("Casual")
length3 = tv_program2.get_length_in_minutes()
minute_count5 = tv_program5.time_left_in_minutes(now)


# special/dunder methods have the double underscores in the method name

class TV_Program:

    def __init__(self, channel, title, start_time):

    def __str__(self):

    def __repr__(self):


# Static / Class method:
# 1. Do NOT deal with an individual object instance
# 2. Common to all object instances
# static class method can be invoked from class name
# Use the decorator @staticmethod to define a static method:

contact_email = Student.admin_email()


# The first argument (cls) of a class method is always referred to the class

class Student:
    email_domain = "solla.sollew.edu"
    student_dir = "/user/student"

    @classmethod
    def admin_email(cls):  # 如果要用到cls里面的类属性，否则不用加
        return "admin@" + cls.email_domain

    @staticmethod
    def uni_website():
        return "http://www.solla.sollew.edu"


# 调用静态函数、类函数：用类名
# 静态方法是从地址上找东西，所以这里是呼唤Student类

print("Uni website: " + Student.uni_website())
print("Admin email: " + Student.admin_email())

# 静态方法 改 类方法
# staticmethod 改 classmethod
# () 改 (cls)
# 点成员、点函数

student1 = Student("0973427", "John", "Smith")
print(shark.name)
angelfish.address = "Uni duck pond"


# 注释函数意思

class Student:
    """
    Class Student represents a student
    """

    def fullname(self):
        """
        Get student's full name
        """
        return self.first_name + " " + self.last_name


# 使用 help(Student) 获取帮助

print(help(Student))


# 定义 学生学号

class Student:

    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        # 生成学号
        self.username = first_name[0].lower() + last_name[0].lower() + id[0:3]

    def email_alias(self):
        """
        Get student's friendly-looking email:
        firstname.lastname.3IDdigits@domain
        """
        return self.first_name + "." + self.last_name + "." + self.id[0:3] + "@"
        + Student.email_domain

    def home_dir(self):
        """
        Get student's Unix home directory:
        studentDir/username
        """
        return Student.student_dir + "/" + self.username

    def fullname(self):
        """
        Get student's full name
        """
        return self.first_name + " " + self.last_name

    def email(self):
        """
        Get student's email: username@domain
        """
        return self.username + "@" + Student.email_domain  # 个人方法使用类属性


student2 = Student("1882845", "Mary", "Wilson")
print(student2.email())
print(student2.email_alias())


# 应用str()到类实例

class Student:

    def __str__(self):
        return "{0} ({1})".format(self.fullname(), self.id)


student2 = Student("1882845", "Mary", "Wilson")
print("Object student2 is " + str(student2))


# 应用repr()到实例

class Student:
    def __repr__(self):
        return "Student('{0}', '{1}', '{2}')". \
            format(self.id, self.first_name, self.last_name)


student2 = Student("1882845", "Mary", "Wilson")
print(repr(student2))


# 多类继承
# Python supports multiple class inheritance:
# a child class can inherit from multiple parent classes.
# Class inheritance allow child class:
# 1. To inherit all parent attributes and methods;
# 2. To override parent attributes;
# 3. To override parent methods.
# 继承，可以重写 类属性 和 类方法

class PostGradStudent(Student):
    # 重载类属性
    student_dir = "/user/poststudent"
    web_domain = "www.solla.sollew.edu"

    def __init__(self, id, first_name, last_name, thesis):  # 原来的+新的
        # 这句话很关键
        super().__init__(id, first_name, last_name)
        # 新的属性
        self.thesis = thesis

    # 增加新函数
    def web_address(self):
        # 这边使用 类属性
        return PostGradStudent.web_domain + "/" + self.username


# 重写分继承和不继承，不继承不用加self，继承要加self和使用super()
# super()是调用上一级的函数

class PostGradStudent(Student):

    def print_detail(self):
        super().print_detail()  # 这边要加东西
        print("Thesis: " + self.thesis)
        print("Web address: " + self.web_address())
