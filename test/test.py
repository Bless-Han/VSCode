class Student:
    def __init__(self, name="book", house="yes"):
        self.name2 = name
        self.house = house

student = Student("harry", "Grffindor")
print(student.name, student.house)
stu = Student()
print(stu.name, stu.house)

import random
a = [1, 2, 3, 4, 5]
print(random.shuffle(a))
a

