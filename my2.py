# Задание 3

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def _middle_grade(self):
        self.mid_grade = sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))
        return self.mid_grade


    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'f'Средняя оценка за домашние задания: {self._middle_grade()}\n'
                f'Курсы в процессе изучения: {",".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {",".join(self.finished_courses)}')


    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Невозможно сравнить!')
            return
        return self.mid_grade < other.mid_grade



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _middle_grade(self):
        self.mid_grade = sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))
        return self.mid_grade

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._middle_grade()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Невозможно сравнить!')
            return
        return self.mid_grade < other.mid_grade



class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res



some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']
some_student.rate_lecturer(some_lecturer, 'Python', 9.9)

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

some_reviewer.rate_hw(some_student, 'Python', 9.9)
some_reviewer.rate_hw(some_student, 'Python', 9.9)
some_reviewer.rate_hw(some_student, 'Python', 9.9)

print(some_reviewer)
print(some_student)
print(some_lecturer)





print("-" * 50)

# Задание 4

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _middle_grade(self):
        self.mid_grade = sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))
        return self.mid_grade

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Курсы в процессе изучения: {",".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {",".join(self.finished_courses)}')

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Невозможно сравнить!')
            return
        return self._middle_grade() < other._middle_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _middle_grade(self):
        self.mid_grade = sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))
        return self.mid_grade

    def __str__(self):
        res = (f'Имя лектора: {self.name}\n'
               f'Фамилия лектора: {self.surname}\n')
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Невозможно сравнить!')
            return
        return self._middle_grade() < other._middle_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n')
        return res


some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']

new_lecturer = Lecturer('Good', 'Buddy')
new_lecturer.courses_attached += ['Git']

old_lecturer = Lecturer('Old', 'Man')
old_lecturer.courses_attached += ['JavaScript']

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python', 'Git', 'JavaScript']
some_student.finished_courses += ['Введение в программирование']
some_student.rate_lecturer(some_lecturer, 'Python', 6.5)
some_student.rate_lecturer(new_lecturer, 'Git', 5.9)
some_student.rate_lecturer(old_lecturer, 'JavaScript', 9.4)

new_student = Student('Every', 'Day', 'your_gender')
new_student.courses_in_progress += ['Python', 'Git', 'JavaScript']
new_student.finished_courses += ['Введение в программирование']
new_student.rate_lecturer(some_lecturer, 'Python', 8.9)
new_student.rate_lecturer(new_lecturer, 'Git', 5.4)
new_student.rate_lecturer(old_lecturer, 'JavaScript', 7.8)

some_reviewer = Reviewer('Every', 'Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.rate_hw(some_student, 'Python', 8.8)
some_reviewer.rate_hw(new_student, 'Python', 5)

easy_reviewer = Reviewer('Just', 'Cause')
easy_reviewer.courses_attached += ['Git', 'JavaScript']
easy_reviewer.rate_hw(some_student, 'Git', 4.7)
easy_reviewer.rate_hw(some_student, 'JavaScript', 6.3)
easy_reviewer.rate_hw(new_student, 'Git', 6.6)
easy_reviewer.rate_hw(new_student, 'JavaScript', 5.7)

students = [some_student, new_student]
marks_python = []
marks_git = []
marks_javascript = []
for student in students:
    for subject, mark in student.grades.items():
        if subject == "Python":
            marks_python.append(mark)
        elif subject == "Git":
            marks_git.append(mark)
        elif subject == "JavaScript":
            marks_javascript.append(mark)
mid_python = sum(sum(marks_python, [])) / len(sum(marks_python, []))
mid_git = sum(sum(marks_git, [])) / len(sum(marks_git, []))
mid_javascript = sum(sum(marks_javascript, [])) / len(sum(marks_javascript, []))

lecturers = [new_lecturer, some_lecturer, old_lecturer]
comment_python = []
comment_git = []
comment_javascript = []
for lecturer in lecturers:
    for subject, mark in lecturer.grades.items():
        if subject == "Python":
            comment_python.append(mark)
        elif subject == "Git":
            comment_git.append(mark)
        elif subject == "JavaScript":
            comment_javascript.append(mark)
teach_python = sum(sum(comment_python, [])) / len(sum(comment_python, []))
teach_git = sum(sum(comment_git, [])) / len(sum(comment_git, []))
teach_javascript = sum(sum(comment_javascript, [])) / len(sum(comment_javascript, []))

print(some_lecturer, f'Средняя оценка за лекции по предмету: {teach_python}\n{some_lecturer.__lt__(new_lecturer)}\n')
print(new_lecturer, f'Средняя оценка за лекции по предмету: {teach_git}\n{new_lecturer.__lt__(old_lecturer)}\n')
print(old_lecturer, f'Средняя оценка за лекции по предмету: {teach_javascript}\n{old_lecturer.__lt__(some_lecturer)}\n')

print(some_student)
print(new_student)
print(f'Средняя оценка за курс Python: {mid_python}\nGit: {mid_git}\nJavaScript: {mid_javascript}\n')

print(some_reviewer)
print(easy_reviewer)
