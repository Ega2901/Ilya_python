import pytest
from .main import Student, GradeProcessor

# Тесты для класса Student
def test_student_creation():
    student = Student(name="Alice", grades=[85, 90])
    assert student.name == "Alice"
    assert student.grades == [85, 90]

def test_student_empty_grades():
    student = Student(name="Bob", grades=[])
    assert student.name == "Bob"
    assert student.grades == []

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

def test_grade_processor_load_data_empty():
    data = {"students": []}
    processor = GradeProcessor(data)
    
    assert len(processor.students) == 0

def test_grade_processor_invalid_data():
    data = {
        "students": [
            {"name": "Alice"},
            {"grades": [78]}
        ]
    }
    
    with pytest.raises(KeyError):
        processor = GradeProcessor(data)

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

def test_generate_grade_combinations_empty_grades():
    data = {
        "students": [
            {"name": "Alice", "grades": []},
            {"name": "Bob", "grades": [78]}
        ]
    }
    
    processor = GradeProcessor(data)
    
    combinations = list(processor.generate_grade_combinations())
    
    assert len(combinations) == 0

def test_generate_grade_combinations_single_student():
    data = {
        "students": [
            {"name": "Alice", "grades": [85]}
        ]
    }
    
    processor = GradeProcessor(data)
    
    combinations = list(processor.generate_grade_combinations())
    
    assert len(combinations) == 1
    assert combinations == [(85,)]

if __name__ == "__main__":
    pytest.main()
