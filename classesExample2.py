class person:
    def __init__(self,name,age,national_id):
        self._name=name 
        self._age =age
        self.__national_id=national_id
    def __str__(self):
        return f"Name: {self._name}, Age: {self._age}, National ID: {self.__national_id}"


class student(person):
    def __init__(self,name,age,national_id,student_id,enrolled_courses):
        super().__init__ (name,age,national_id)
        self.student_id=student_id
        self.enrolled_courses=enrolled_courses
    def enroll(self,course):
        self.enrolled_courses.append(course)
    def get_student_info(self):
       base =super().__str__() 
       print( f"{base} ,Student ID: {self.student_id} enrolled courses: {self.enrolled_courses}")


class teacher(person):
    def __init__(self,name,age,national_id,teacher_id, courses_teaching):
        super().__init__ (name,age,national_id)
        self.teacher_id=teacher_id
        self.courses_teaching=courses_teaching

    def grade_student(self, student, course, grade):
        if student in course.grades:
            course.set_grade(student, grade)
        else:
            print("Student is not enrolled in this course.")

    def get_teacher_info(self):
       base= super().__str__() 
       print( f"{base} ,teacher ID: {self.teacher_id} teached_courses: {self.courses_teaching}")


class course:
    def __init__(self,course_name,course_code,grades):
        self.course_name=course_name
        self.course_code=course_code
        self.grades=grades
    def add_student(self,student):
        self.grades[student]=0 
        student.enroll(self.course_name)

    def set_grade(self,student,grade):
        if student in self.grades:
            self.grades[student] = grade
        else:
            print(f"Student {student._name} is not enrolled in this course.")
    def get_student_grades(self):   
        print(f"Grades for {self.course_name}:")
        for student in self.grades:
           print( f"student: {student._name}, grade {self.grades[student]}" )

math = course("Math", "M101", {})
english = course("English", "ENG101", {})

s1 = student("Yara", 18, "123456789", "S100", [])
s2 = student("Laila", 19, "222222222", "S101", [])

t1 = teacher("Dr. Ahmed", 40, "987654321", "T200", [])

math.add_student(s1)
math.add_student(s2)
t1.courses_teaching.append("math")

t1.grade_student(s1, math, 90)
t1.grade_student(s2, math, 85)

s1.get_student_info()
t1.get_teacher_info()
math.get_student_grades()
