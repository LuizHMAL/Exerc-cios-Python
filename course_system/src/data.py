import json
from src.student import Student
from src.teacher import Teacher
from src.course import Course
from src.course_management import CourseManagement

DATA_FILE = "data.json"

def load_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        return CourseManagement([]), [], []

  
    students_dict = {}
    for s in data.get("students", []):
        student = Student(s["name"], s["id"])
        student.scores = s.get("scores", {})
        students_dict[student.id] = student


    courses = []
    for c in data.get("courses", []):
        course_students = [students_dict[s["id"]] for s in c.get("students", []) if s["id"] in students_dict]
        course = Course(
            c["id"],
            c["name"],
            c["hours"],
            course_students,
            c["min_score"]
        )
        courses.append(course)

 
    teachers = []
    for t in data.get("teachers", []):
        teacher = Teacher(t["id"], t["name"], t["teaching_hours"])
        teachers.append(teacher)

    return CourseManagement(courses), list(students_dict.values()), teachers

def save_data(course_mgmt: CourseManagement, students: list, teachers: list):
    data = {
        "courses": [],
        "students": [],
        "teachers": []
    }

    for c in course_mgmt.get_course_list():
        data["courses"].append({
            "id": c.id,
            "name": c.name,
            "hours": c.hours,
            "min_score": c.min_score,
            "students": [{"id": s.id, "name": s.name} for s in c.students]
        })


    for s in students:
        data["students"].append({
            "id": s.id,
            "name": s.name,
            "scores": s.scores
        })

    for t in teachers:
        data["teachers"].append({
            "id": t.id,
            "name": t.name,
            "teaching_hours": t.teaching_hours
        })

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)