from src.course import Course
from src.student import Student
from src.data import load_data, save_data

class Interaction:
    def __init__(self):
        self.course_management, self.students, self.teachers = load_data()

    def start(self):
        while True:
            print("\n=== SISTEMA ACADÊMICO ===")
            print("Quem está acessando?")
            print("1. Gerente")
            print("2. Professor")
            print("3. Estudante")
            print("0. Sair")
            try:
                role = int(input("Sua escolha: "))
            except ValueError:
                print("Opção inválida.")
                continue

            match role:
                case 1: self.menu_gerente()
                case 2: self.menu_professor()
                case 3: self.menu_estudante()
                case 0:
                    print("Encerrando...")
                    break
                case _: print("Opção inválida.")


    def menu_gerente(self):
        while True:
            print("\n--- Menu Gerente ---")
            print("1. Listar cursos")
            print("2. Criar curso")
            print("3. Ver aprovados por curso")
            print("0. Voltar")
            try:
                op = int(input("Escolha: "))
            except ValueError:
                continue

            match op:
                case 1: self.list_all_courses()
                case 2: self.create_course()
                case 3: self.show_approved_students()
                case 0: break
                case _: print("Opção inválida.")

    def menu_professor(self):
        while True:
            print("\n--- Menu Professor ---")
            print("1. Listar cursos")
            print("2. Listar alunos de curso")
            print("3. Adicionar aluno a curso")
            print("4. Remover aluno de curso")
            print("5. Avaliar aluno")
            print("6. Ver aprovados por curso")
            print("7. Ver média de um aluno")
            print("0. Voltar")
            try:
                op = int(input("Escolha: "))
            except ValueError:
                continue

            match op:
                case 1: self.list_all_courses()
                case 2: self.list_students_by_course()
                case 3: self.add_student_to_course()
                case 4: self.remove_student_from_course()
                case 5: self.evaluate_student()
                case 6: self.show_approved_students()
                case 7: self.show_student_average()
                case 0: break
                case _: print("Opção inválida.")


    def menu_estudante(self):
        while True:
            print("\n--- Menu Estudante ---")
            print("1. Ver aprovados por curso")
            print("2. Ver minha média")
            print("0. Voltar")
            try:
                op = int(input("Escolha: "))
            except ValueError:
                continue

            match op:
                case 1: self.show_approved_students()
                case 2: self.show_student_average()
                case 0: break
                case _: print("Opção inválida.")


    def list_all_courses(self):
        courses = self.course_management.get_course_list()
        if not courses:
            print("Nenhum curso encontrado.")
            return
        for course in courses:
            print(f"{course.id} - {course.name} ({course.hours}h) - Nota mínima: {course.min_score}")

    def list_students_by_course(self):
        cid = input("ID do curso: ")
        course = self.course_management.get_course(cid)
        if not course:
            print("Curso não encontrado.")
            return
        if not course.students:
            print("Nenhum aluno no curso.")
        for s in course.students:
            print(f"{s.id} - {s.name}")

    def create_course(self):
        cid = input("ID do curso: ")
        name = input("Nome do curso: ")
        try:
            hours = int(input("Carga horária: "))
            min_score = float(input("Nota mínima: "))
        except ValueError:
            print("Erro nos dados.")
            return
        course = Course(cid, name, hours, [], min_score)
        self.course_management.add_course(course)
        print("Curso criado com sucesso.")
        self._save()

    def add_student_to_course(self):
        sid = input("ID do aluno: ")
        name = input("Nome do aluno: ")
        cid = input("ID do curso: ")

        student = self._get_or_create_student(sid, name)
        self.course_management.add_student_to_course(cid, student)
        print("Aluno adicionado.")
        self._save()

    def remove_student_from_course(self):
        cid = input("ID do curso: ")
        sid = input("ID do aluno: ")
        student = self.course_management.get_student_by_id(sid)
        if student:
            self.course_management.remove_student_from_course(cid, student)
            print("Aluno removido.")
            self._save()
        else:
            print("Aluno não encontrado.")

    def evaluate_student(self):
        sid = input("ID do aluno: ")
        cid = input("ID do curso: ")
        try:
            score = float(input("Nota: "))
        except ValueError:
            print("Nota inválida.")
            return
        student = self.course_management.get_student_by_id(sid)
        if not student:
            print("Aluno não encontrado.")
            return
        student.scores[cid] = score
        print("Nota atribuída.")
        self._save()

    def show_approved_students(self):
        approved = self.course_management.approved_by_course()
        if not approved:
            print("Nenhum aprovado.")
            return
        for course, medias in approved.items():
            print(f"\nCurso: {course}")
            for m in medias:
                print(f"Média: {m:.2f}")

    def show_student_average(self):
        sid = input("ID do aluno: ")
        avg = self.course_management.student_average_score(sid)
        if avg is None:
            print("Aluno não encontrado ou sem notas.")
        else:
            print(f"Média do aluno: {avg:.2f}")



    def _get_or_create_student(self, sid: str, name: str) -> Student:
        for s in self.students:
            if s.id == sid:
                return s
        s = Student(name, sid)
        self.students.append(s)
        return s

    def _save(self):
        save_data(self.course_management, self.students, self.teachers)