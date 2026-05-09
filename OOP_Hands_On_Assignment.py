import random

class Student:
    def __init__(self, name:str, email:str, grades:list=[]):
        self.name = name
        self.email = email
        self.grades = grades

    # Use to add a grade to the grades list. Grades list is empty by default
    def add_grade(self, grade:int):
        self.grades.append(int(grade))

    # Will only do the calculation if the grades list isn't empty.
    def average_grade(self) -> int:
        if self.grades == []:
            return 0
        else:
            return int(sum(self.grades) / len(self.grades))
    
    # Displays formatted information about a student. 
    def display_info(self) -> str:
        return f"Student name: {self.name}, Student Email: {self.email}, Student's grades: {self.grades}"

# Function that uses the student_dict to retrieve a student's object via their email.
def get_student_by_email(email:str):
    return student_dict.get(email)

# Runs 2 inline for loops to get a set of all the grades from every student.
def get_all_unique_grades(students:dict):
    return {grade for student in students.values() for grade in student.grades}

# Each student is given random starting grades.
student1 = Student("George", "Gman112@gmail.com", [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)])
student2 = Student("Larry", "LARSmith@gmail.com", [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)])
student3 = Student("Kristina", "KristyMist@gmail.com", [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)])

student_dict = {
    student1.email : student1,
    student2.email : student2,
    student3.email : student3,
}

# Adds 2 new random grades to each student.
student1.add_grade(random.randint(0, 100))
student1.add_grade(random.randint(0, 100))

student2.add_grade(random.randint(0, 100))
student2.add_grade(random.randint(0, 100))

student3.add_grade(random.randint(0, 100))
student3.add_grade(random.randint(0, 100))


# print(student1.display_info())
# print(student1.average_grade())
# print(get_student_by_email("Gman112@gmail.com"))

# print(student2.display_info())
# print(student2.average_grade())

# print(student3.display_info())
# print(student3.average_grade())

print(f"All unique grades from each student: {get_all_unique_grades(student_dict)}")