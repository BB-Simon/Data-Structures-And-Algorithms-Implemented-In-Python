import re


class Person:
    def __init__(self, name: str, date_of_birth: int, age: int = None):
        self.__name = name
        self.__DOB = date_of_birth
        self.__age = age

    def get_dob(self):
        return self.__DOB

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if self.__is_name_valid(new_name):
            print("name can't include a number")
            return
        self.__name = new_name

    def __is_name_valid(self, new_name):
        return re.search(r"[0-9]", new_name)

    def get_sumary(self):
        pass
        # return f"Name is: {self.__name}, DOB is: {self.__DOB}, Age is: {self.__age if self.__age is not None else 'Not Metioned'} "


# person_one = Person("Simon", 1992, "simon@email.com")
# # print(person_one.get_name())
# print(person_one.get_sumary())
# print("-" * 20)
# person_one.set_name("jimon")
# print(person_one.get_name())


# person_list = [
#     Person("Simon", 1992, 28),
#     Person("Jimon", 1994, 26),
#     Person("Takmina", 1997),
#     Person("Souvo", 2026),
#     Person("Jannat", 2015),
#     Person("someone", 1989),
#     Person("somoneelse", 1988),
# ]

# for person in person_list:
#     if person.get_dob() >= 1990:
#         print(person.get_sumary())


class Student(Person):
    def __init__(self, name: str, date_of_birth: int, email_id: str, student_id: str):
        super().__init__(name, date_of_birth)
        self.email = email_id
        self.student_id = student_id

    def get_sumary(self):
        return f"Name: {self.get_name()}, Email: {self.email}, DOB: {self.get_dob()}"

    def __str__(self):
        return self.get_sumary()

    def __repr__(self):
        return self.get_sumary() 


student = Student("a", 1992, "simon@email.com", "00111232")
print(student)
student.set_name("simon")
print("-"*20)
print(student)


class Teacher(Person):
    def __init__(self, name: str, date_of_birth: int, department: str):
        super().__init__(name, date_of_birth)
        self.department = department

    def get_sumary(self):
        return f"{self.get_name()} is a teacher"


new_person_list = [
    Person('Simon', 1992, 28),
    Student("Jimon", 1994, "jimon@email.com", "008898"),
    Teacher("Takmina", 1997, "Math")
]

for p in new_person_list:
    print(p.get_sumary())