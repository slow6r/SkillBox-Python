class Student:
    def __init__(self, name, group, grades):
        self.name = name
        self.group = group
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

students = [
    Student("Иван Иванов", "Группа 1", [4, 5, 3, 4, 5]),
    Student("Петр Петров", "Группа 1", [5, 5, 5, 5, 5]),
    Student("Мария Сидорова", "Группа 2", [3, 4, 4, 4, 4]),
    Student("Ольга Смирнова", "Группа 2", [4, 4, 4, 4, 4]),
    Student("Дмитрий Кузнецов", "Группа 3", [5, 5, 5, 4, 4]),
    Student("Анна Орлова", "Группа 3", [3, 4, 3, 3, 4]),
    Student("Николай Тихонов", "Группа 4", [5, 4, 4, 5, 5]),
    Student("Елена Новикова", "Группа 4", [5, 3, 4, 5, 4]),
    Student("Сергей Федоров", "Группа 5", [3, 4, 4, 4, 3]),
    Student("Алексей Павлов", "Группа 5", [4, 5, 5, 4, 5])
]

students.sort(key=lambda student: student.average_grade())

print("Список студентов, отсортированный по среднему баллу:")
for student in students:
    print(f"{student.name}, группа {student.group}, средний балл: {student.average_grade():.2f}")
