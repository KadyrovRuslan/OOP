class Student:
    students_list = []

    def __init__(self, name, surname, gender):
      self.name = name
      self.surname = surname
      self.gender = gender
      self.finished_courses = []
      self.courses_in_progress = []
      self.grades = {}
      self.students_list.append(self)

    def overall_average(self):
      average_mark(sum(self.grades.values(), []))
      return 

    def rate_lection(self, lecture, course, grade):
      if isinstance(lecture, Lecture) and course in self.courses_in_progress and course in lecture.courses_attached:
        if course in lecture.grades:
          lecture.grades[course] += [grade]
        else:
          lecture.grades[course] = [grade]
      else:
        return 'Ошибка'

    def __str__(self):
      return f'Студент\nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашнее задание:  {average_mark(sum(self.grades.values(), []))} \nКурсы в процессе изучения:  {", ".join(self.courses_in_progress)} \nЗавершенные курсы:  {", ".join(self.finished_courses)}'

    def __lt__(self, other):
      self.overall_average < other.overall_average
      return

class Mentor:
  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
    self.courses_attached = []

class Lecture(Mentor):
    lectures_list = []

    def __init__(self, name, surname):
      super().__init__(name, surname)
      self.grades = {}
      self.lectures_list.append(self)

    def overall_average(self):
      average_mark(sum(self.grades.values(), []))
      return 

    def __str__(self):
      return f'Лектор\nИмя: {self.name}\nФамилия: {self.surname} \nСредняя оценка за лекции:{average_mark(sum(self.grades.values(), []))}'

    def __lt__(self, other):
      self.overall_average < other.overall_average
      return 


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
      return str('Рецензент\nИмя: ' + self.name + '\n' + 'Фамилия: ' + self.surname)

def average_mark(marks: list):
  if marks:
    return sum(marks) / len(marks)

def mark_hw_course(students: list, course: str):
    marks_hw = []
    for student in students:
      marks_hw.append(average_mark(student.grades[course]))
    return average_mark(marks_hw)

def mark_lection_course(lectures: list, course: str):
    marks_l = []
    for lecture in lectures:
      marks_l.append(average_mark(lecture.grades[course]))
    return average_mark(marks_l)

student_1 = Student('Сергей', 'Юдин', 'gender')
student_1.courses_in_progress += ['Git', 'Python']
student_1.finished_courses += ['ООП: объекты и классы. Взаимодействие между ними', 'Git — система контроля версий']

student_2 = Student('Григорий', 'Захарьин', 'gender')
student_2.courses_in_progress += ['Git', 'Python']
student_2.finished_courses += ['ООП: объекты и классы. Взаимодействие между ними', 'Git — система контроля версий']

expert_1 = Reviewer('Николай', 'Склифосовский')
expert_1.courses_attached += ['Git', 'Python']
expert_1.rate_hw(student_1, 'Git', 10)
expert_1.rate_hw(student_1, 'Python', 9)

expert_2 = Reviewer('Иван', 'Павлов')
expert_2.courses_attached += ['Git', 'Python']
expert_2.rate_hw(student_2, 'Git', 4)
expert_2.rate_hw(student_2, 'Python', 5)

Lecturer_1 = Lecture('Владимир', 'Филатов')
Lecturer_1.courses_attached += ['Git', 'Python']
Lecturer_2 = Lecture('Гавриил', 'Илизаров')
Lecturer_2.courses_attached += ['Git', 'Python']

student_1.rate_lection(Lecturer_1, 'Git', 8)
student_1.rate_lection(Lecturer_1, 'Python', 9)
student_1.rate_lection(Lecturer_2, 'Git', 9)
student_1.rate_lection(Lecturer_2, 'Python', 10)

print(f'{expert_1} \n{expert_2} \n') 
print(f'{Lecturer_1} \n{Lecturer_2} \n')
print(f'{student_1} \n{student_2} \n')

print('\n' + "Подсчет средней оценки за домашние задания по всем студентам в рамках конкретного курса:")
print('Git',(mark_hw_course(Student.students_list, 'Git')))
print('Python',(mark_hw_course(Student.students_list, 'Python')))

print('\n' + "Подсчет средней оценки за лекции всех лекторов в рамках конкретного курса:")
print ('Git',(mark_lection_course(Lecture.lectures_list, 'Git'))) 
print ('Python',(mark_lection_course(Lecture.lectures_list, 'Python')))