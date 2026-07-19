# person class (parent)
class Person():
    def __init__(self, name: str, age: str):
        self.name = name
        self.age = age

    def display_info(self):
        print("--student info--")
        print(f"Name: {self.name}\nAge: {self.age}")


# student class (child of person)
class Student(Person):
    def __init__(self, name: str, age: str, student_id: str, marks: dict):
        super().__init__(name,age)
        self.__student_id = student_id
        self.__marks = marks

    @property
    def student_id(self):
        return self.__student_id
    
    @property
    def marks(self):
        return self.__marks

    def add_subject(self, subject: str, mark: float):
        if subject not in self.__marks:
            self.__marks[subject] = mark
        else:
            print("Subject already exists.")

    def update_marks(self, subject: str, mark: float):
        if subject not in self.__marks:
            print("Subject doesn't exists.")
        else:
            self.__marks[subject] = mark

    def remove_subject(self, subject: str):
        if subject not in self.__marks:
            print("Subject doesn't exists.")
        else:
            self.__marks.pop(subject)

    def calculate_average(self):
        if not self.__marks:
            return 0
        return sum(self.__marks.values()) / len(self.__marks)
    
    def display_info(self):
        super().display_info()
        print(f"Student Id: {self.__student_id}\nMarks: {self.__marks}")
    
# Graduate Student class (inherits Student)
class Graduate_Student(Student):
    def __init__(self, name: str, age: str, student_id: str, marks: dict, thesis_title: str):
        super().__init__(name, age, student_id, marks)
        self.__thesis_title = thesis_title

    def display_info(self):
        super().display_info()
        print(f"Thesis title: {self.__thesis_title}")


# Student Management Class
class Student_Management():
    def __init__(self):
        self.students_detail = {}

    def add_student(self, student: Student):
        if student.student_id not in self.students_detail:
            self.students_detail[student.student_id] = student
        else:
            print("Student already exists.")
    
    def remove_student(self, student_id: str):
        if student_id in self.students_detail:
            self.students_detail.pop(student_id)
        else:
            print("Student not found.")

    def search_student(self, student_id: str):
        if student_id in self.students_detail:
            print("\nStudent found.")
            self.students_detail[student_id].display_info()
        else:
            print("Student not found.")

    def display_topper(self):
        topper = None
        max_avg = -1
        for student in self.students_detail.values():
            avg = student.calculate_average()

            if avg > max_avg:
                topper = student
                max_avg = avg

        print("\nTopper student details")
        topper.display_info()

    def failed_student(self):
        for student in self.students_detail.values():
            for mark in student.marks.values():
                if mark < 40:
                    student.display_info()
                    break

    def display_all_students(self):
        if not self.students_detail:
            print("No students found.")
            return

        for student in self.students_detail.values():
            student.display_info()
            print("\n")



def main():
    s1 = Student("Ram","12","0001",{"eng": 15, "math": 45})
    s2 = Student("Shyam","13","0032",{"eng": 64, "math": 50})
    g1 = Graduate_Student("hari","31","1000",{"eng": 35, "math": 95}, "AI")
    g2 = Graduate_Student("hari","24","1012",{"eng": 25, "math": 55}, "Web")
    
    wrc = Student_Management()

    wrc.add_student(s1)
    wrc.add_student(s2)
    wrc.add_student(g1)
    # wrc.remove_student("0001")
    # wrc.search_student("0001")

    wrc.display_all_students()
    # wrc.display_topper()
    wrc.failed_student()

if __name__ == "__main__":
    main()