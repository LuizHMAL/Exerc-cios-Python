from src.student import Student


class Course:
    def __init__(self, id: str, name: str, hours: int, students: list[Student], min_score: float):
        self.id = id
        self.name = name
        self.hours = hours
        self.students = students
        self.min_score = min_score
    
    