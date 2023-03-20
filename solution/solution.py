class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} {self.house}"

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin", "SY"]:
            raise ValueError("Invalid house")
        self._house = house

def main():
    s = Student("Neo", "SY")
    s.house = "Gryffindor"
    print(s)

main()
