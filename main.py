class Mentor:
  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
    self.courses_attached = []

class Lecturer(Mentor):
  def __init__(self, name, surname):
    super().__init__(name, surname)
    self.grades = {}

  def receive_grade(self, course: str, grade: int) -> None:
    self.grades.setdefault(course, []).append(grade)

  def get_grades(self, course: str) -> list[int]:
        return self.grades.get(course, [])
  
  def average(self, course: str) -> float:
        marks = self.grades.get(course, [])
        return sum(marks) / len(marks) if marks else 0.0
  
  def overall_average(self) -> float:
        all_marks = [g for marks in self.grades.values() for g in marks]
        return sum(all_marks) / len(all_marks) if all_marks else 0.0
  
  def __str__(self):
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за лекции: {self.overall_average():.1f}'
        )
  
  def __repr__(self):
        return f'Lecturer({self.name!r}, courses={self.courses_attached})'

class Reviewer(Mentor):
  def rate_hw(self, student, course, grade):
    if (
        isinstance(student, Student) 
        and course in self.courses_attached 
        and course in student.courses_in_progress
    ):
        student.grades.setdefault(course, []).append(grade)
    else:
        return 'Ошибка'
    
  def __str__(self):
     return f'Имя: {self.name}\nФамилия: {self.surname}'
    
class Student:
  def __init__(self, name, surname, gender):
    self.name = name
    self.surname = surname
    self.gender = gender
    self.finished_courses = []
    self.courses_in_progress = []
    self.grades = {}

  def rate_lecturer(self, lecturer: Lecturer, course: str, grade: int):
    if (
       isinstance(lecturer, Lecturer)
       and course in lecturer.courses_attached
       and course in self.courses_in_progress
       and 1 <= grade <= 10
    ):
       lecturer.receive_grade(course, grade)
    else:
       return 'Ошибка'
    
    def overall_average(self) -> float:
        all_marks = [g for marks in self.grades.values() for g in marks]
        return sum(all_marks) / len(all_marks) if all_marks else 0.0

    def __str__(self):
        in_progress = ', '.join(self.courses_in_progress) if self.courses_in_progress else 'Нет'
        finished = ', '.join(self.finished_courses) if self.finished_courses else 'Нет'
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {self.overall_average():.1f}\n"
            f"Курсы в процессе изучения: {in_progress}\n"
            f"Завершенные курсы: {finished}"
        )

  def __repr__(self):
        return f'Student({self.name!r}, courses={sorted(self.courses_in_progress)})'

reviewer = Reviewer('Some', 'Buddy')
reviewer.courses_attached += ['Python', 'Git']

lecturer = Lecturer('Some', 'Buddy')
lecturer.courses_attached += ['Python', 'Git']

student = Student('Ruoy', 'Eman', 'male')
student.courses_in_progress += ['Python', 'Git']
student.finished_courses += ['Введение в программирование']

reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student, 'Git', 9.8)
student.rate_lecturer(lecturer, 'Python', 10)
student.rate_lecturer(lecturer, 'Git', 9.8)

print(reviewer)
print()
print(lecturer)
print()
print(student)