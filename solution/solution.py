students = [
        {"name": "Ron", "house": "Gryffindor"},
        {"name": "Draco", "house": "Slytherin"},
        {"name": "Hermione", "house": "Gryffindor"},
        {"name": "Harry", "house": "Gryffindor"},
        ]

def main():

    for student in sorted(students, key=get_name):
        print(student["name"], student["house"])

def get_name(student):
    return student["name"]

main()

print("OK")


'''
Draco is in Slytherin
Harry is in Gryffindor
Hermione is in Gryffindor
Ron is in Gryffindor
'''
