'''module docstring'''
import random


class Student:
    '''class docstring'''
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school

    def introduce_self(self):
        '''method docstring'''
        return f'Hello, my name is {self.name}, I am {self.age} years old and I attend {self.school}'

    def birthday(self):
        '''method docstring'''
        self.age += 1


class BloomTechStudent(Student):
    '''class docstring'''    
    def __init__(self, name, age, school, track, cohort):
        super().__init__(name, age, school)
        self.track = track
        self.cohort = cohort
        self.graduated = False

    def flex(self):
        self.cohort += 1

    def graduate(self):
        self.graduated = True


def student_generator(num_students=30):
    '''function docstring'''
    first_names = ['Arthur', 'Becky', 'Darrel', 'Eric', 'Francine', 'Gary']
    last_names = ['Adams', 'Brown', 'Douglas', 'Evans', 'Farnsworth', 'Gunderson']

    students = []

    for _ in range(num_students):
        random_first_name = random.choice(first_names)
        random_last_name = random.choice(last_names)
        random_name = random_first_name + ' ' + random_last_name
        age = random.randint(18, 100)
        school = 'Bloomtech'
        track = random.choice(['WEB', 'DS', 'Backend'])
        cohort = random.randint(1, 50)

        students.append(BloomTechStudent(random_name, age, school, track, cohort))

    return students


student_list = student_generator()

for student in student_list:
    print(student.introduce_self())

# Uncomment the following lines to test other methods
# print(student_list[0].name)
# print(student_list[0].age)
# print(student_list[0].school)
# print(student_list[0].introduce_self())
# student_list[0].birthday()
# print(student_list[0].age)
# print(student_list[0].track)
# print(student_list[0].cohort)
# student_list[0].flex()
# print(student_list[0].cohort)
# student_list[0].graduate()
# print(student_list[0].graduated)