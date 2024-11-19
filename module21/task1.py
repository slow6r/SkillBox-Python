# Исходные данные
students = {
    1: {'name': 'Bob', 'surname': 'Vazovski', 'age': 23, 'interests': ['biology, swimming']},
    2: {'name': 'Rob', 'surname': 'Stepanov', 'age': 24, 'interests': ['math', 'computer games', 'running']},
    3: {'name': 'Alexander', 'surname': 'Krug', 'age': 22, 'interests': ['languages', 'health food']}
}

# Функция для обработки данных
def analyze_students(data):
    interests = {interest for student in data.values() for interest in student['interests']}
    total_surname_length = sum(len(student['surname']) for student in data.values())
    return interests, total_surname_length

# Список пар "ID студента — возраст"
pairs = [(student_id, info['age']) for student_id, info in students.items()]
print(f"Список пар 'ID студента — возраст': {pairs}")

# Анализ интересов и длины фамилий
interests, surname_length = analyze_students(students)
print(f"Полный список интересов всех студентов: {interests}")
print(f"Общая длина всех фамилий студентов: {surname_length}")
