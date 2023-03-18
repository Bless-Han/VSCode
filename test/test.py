class Student:
    def __init__(self, name="book", house="yes"):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

student = Student("harry", "Grffindor")
print(student.name, student.house)
print(student)
