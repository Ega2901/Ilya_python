import json
from itertools import product
from dataclasses import dataclass

@dataclass
class Student:
    """Класс для представления студента.

    Attributes:
        name (str): Имя студента.
        grades (list): Список оценок студента.
    """

class GradeProcessor:
    """Класс для обработки оценок студентов.

    Attributes:
        students (list): Список объектов Student.
    """

    def __init__(self, data):
        """Инициализация GradeProcessor с данными студентов.

        Args:
            data (dict): Словарь с данными студентов.
        """
        pass

    def load_data(self, data):
        """Загрузка данных студентов из словаря.

        Args:
            data (dict): Словарь с данными студентов.

        Returns:
            list: Список объектов Student.
        """
        pass

    def generate_grade_combinations(self):
        """Генерация всех возможных комбинаций оценок студентов.

        Yields:
            tuple: Комбинация оценок.
        """
        pass

    def process_students(self):
        """Обработка и вывод информации о студентах."""
        pass

