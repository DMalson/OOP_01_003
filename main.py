class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in (self.courses_in_progress + self.finished_courses) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self) :
        newstring = 'Имя: ' + self.name + '\n'
        newstring += 'Фамилия: ' + self.surname + '\n'
        newstring += 'Средняя оценка за домашние задания: ' + str(self.av_grade()) + '\n'
        newstring += 'Курсы в процессе изучения: ' + ', '.join(self.courses_in_progress) + '\n'
        newstring += 'Завершенные курсы: '  + ', '.join(self.finished_courses) + '\n'
        return(newstring)

    def av_grade(self):
        gradesum = 0
        numgrades = 0
        for gradelist in self.grades.values():
            numgrades += len(gradelist)
            for grade in gradelist:
                gradesum += grade
        return gradesum / numgrades

    def __lt__(self, other) :
        if not(isinstance(other, Student)):
            return 'Ошибка'
        if self.av_grade() < other.av_grade() :
            return True
        else:
            return False

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def av_grade(self):
        gradesum = 0
        numgrades = 0
        for gradelist in self.grades.values():
            numgrades += len(gradelist)
            for grade in gradelist:
                gradesum += grade
        return gradesum / numgrades

    def __str__(self) :
        newstring = 'Имя: ' + self.name + '\n'
        newstring += 'Фамилия: ' + self.surname + '\n'
        newstring += 'Средняя оценка за лекции: ' + str(self.av_grade())
        return(newstring)

    def __lt__(self, other) :
        if not(isinstance(other, Lecturer)):
            return 'Ошибка'
        if self.av_grade() < other.av_grade() :
            return True
        else:
            return False


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Java', 'Python']
best_student.finished_courses += ['C#', 'Javascript']
real_student = Student('Иван', 'Петров', 'male')
real_student.courses_in_progress += ['Java', 'Python']
real_student.finished_courses += ['C#', 'Javascript']

cool_mentor = Lecturer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python', 'Java']
nice_mentor = Lecturer('Nice', 'Lady')
nice_mentor.courses_attached += ['C#', 'Java']

stern_reviewer = Reviewer("Ned", "Stark")
stern_reviewer.courses_attached += ['Python', 'Java']

stern_reviewer.rate_hw(best_student, 'Python', 7)
stern_reviewer.rate_hw(best_student, 'Java', 6)
stern_reviewer.rate_hw(best_student, 'Python', 8)
stern_reviewer.rate_hw(real_student, 'Python', 6)

best_student.rate_hw(cool_mentor, 'Python', 9)
best_student.rate_hw(cool_mentor, 'Java', 10)
best_student.rate_hw(cool_mentor, 'Java', 5)
best_student.rate_hw(nice_mentor, 'Java', 10)

print(best_student.grades)
print(cool_mentor.grades)
print(best_student)
print(cool_mentor)
print(cool_mentor > nice_mentor)
print(best_student > real_student)
