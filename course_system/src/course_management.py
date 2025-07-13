from .course import Course
from .student import Student

class CourseManagement:
    def __init__(self, courses: list[Course]):
        self.courses = courses

    @property
    def students(self) -> list[Student]:
        return [student for course in self.courses for student in course.students]

    def add_course(self, course: Course):
        self.courses.append(course)

    def get_course_list(self) -> list[Course]:
        return self.courses

    def get_course(self, course_id: str) -> Course | None:
        for course in self.courses:
            if course.id == course_id:
                return course
        return None

    def add_student_to_course(self, course_id: str, student: Student):
        for course in self.courses:
            if course.id == course_id:
                if student not in course.students:
                    course.students.append(student)
                return

    def remove_student_from_course(self, course_id: str, student: Student):
        for course in self.courses:
            if course.id == course_id:
                if student in course.students:
                    course.students.remove(student)
                return

    def get_student(self, student_id: str) -> Student | None:
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    def get_student_by_id(self, student_id: str) -> Student | None:
        return self.get_student(student_id)

    def student_average_score(self, student_id: str) -> float | None:
        student = self.get_student_by_id(student_id)
        if student is None or not student.scores:
            return None
        return sum(student.scores.values()) / len(student.scores)

    def approved_by_course(self) -> dict[str, list[float]]:
        approved_students = {}
        for course in self.courses:
            min_score = course.min_score
            for student in course.students:
                avg = self.student_average_score(student.id)
                if avg is not None and avg >= min_score:
                    if course.name not in approved_students:
                        approved_students[course.name] = []
                    approved_students[course.name].append(avg)
        return approved_students
