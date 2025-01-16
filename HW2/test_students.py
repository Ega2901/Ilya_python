import pytest
from main import Student, GradeProcessor

# Тесты для класса Student
def test_student_creation():
    student = Student(name="Alice", grades=[85, 90])
    assert student.name == "Alice"
    assert student.grades == [85, 90]

# Тесты для класса GradeProcessor
def test_grade_processor_load_data():
    data = {
        "students": [
            {"name": "Alice", "grades": [85, 90]},
            {"name": "Bob", "grades": [78, 82]}
        ]
    }
    
    processor = GradeProcessor(data)
    
    assert len(processor.students) == 2
    assert processor.students[0].name == "Alice"
    assert processor.students[1].grades == [78, 82]

def test_generate_grade_combinations():
    data = {
        "students": [
            {"name": "Alice", "grades": [85, 90]},
            {"name": "Bob", "grades": [78]}
        ]
    }
    
    processor = GradeProcessor(data)
    
    combinations = list(processor.generate_grade_combinations())
    
    assert len(combinations) == 2
    assert combinations == [(85, 78), (90, 78)]

if __name__ == "__main__":
    pytest.main()
