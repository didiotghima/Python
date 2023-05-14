# class Person:
#     def __init__(self, fullname, age, is_married):
#         self.fullname = fullname
#         self.age = age
#         self.is_married = is_married

#     def introduce_myself(self):
#         print(f"Меня зовут {self.fullname}. Мне {self.age} лет. {'Я не женат.'}")


# person = Person("Кыдыров Асхат", 17, True )
# person.introduce_myself()

# class Student(Person):
#     def __init__(self, fullname, age, is_married, marks):
#         super().__init__(fullname, age, is_married)
#         self.marks = marks

#     def calculate_average_mark(self):
#         total_marks = sum(self.marks.values())
#         return total_marks / len(self.marks)

# student = Student("Кыдыров Асхат", 20, False, {"фискультура": 2, "История": 3, "английский": 4})
# student.introduce_myself() 
# print(student.calculate_average_mark())

# class Teacher(Person):
#     def __init__(self, fullname, age, is_married, experience, salary):
#         super().__init__(fullname, age, is_married)
#         self.experience = experience
#         self.salary = salary

#     def calculate_salary(self):
#         base_salary = self.salary
#         if self.experience > 3:
#             bonus = (self.experience - 3) * 0.05 * base_salary
#             return base_salary + bonus
#         else:
#             return base_salary

# def create_students():
#     student1 = Student("Даня Александрович", 16, False, {"химия": 4, "биология": 4, "история": 2})
#     student2 = Student("Большая Мачеха", 17, False, {"химия": 5, "биология": 4, "история": 4})
#     student3 = Student("Дядя Отчима", 17, False, {"химия": 5, "биология": 4, "история": 2})
#     return [student1, student2, student3]


# students = create_students()
# for student in students:
#     student.introduce_myself()
#     for subject, mark in student.marks.items():
#         print(f"{subject}: {mark}")
#     average_mark = student.calculate_average_mark()
#     print(f"Average mark: {average_mark:.2f}")
