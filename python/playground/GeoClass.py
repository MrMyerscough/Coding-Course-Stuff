class Geometry:
    """This class will handle different aspects of our high school
    geometry class, such as grading and student records."""

    def __init__(self, students: list, grades: list, MAP: list, student_grade: list) -> None:
        newStudents = []
        for student in students:
            newStudents.append(student.rstrip())
        self.students = newStudents[:]
        self.grades = grades[:]
        self.MAP = MAP[:]
        self.student_grade = student_grade[:]

    # This function will search the students list for the student that you want to check the average standard grade for,
    # return the index for that student, and then use that index to search the grades list for their average standard grade.
    def check_grade(self):
        student = input("Which student do you want to check the grade for? ")
        #student.strip()
        #student.lower()
        if student in self.students[:]:
            student_num = self.students.index(student)
            print(student + "'s grade is " + self.grades[student_num])
        else:
            print ("That student isn't in this class!")

    # This function will search the students list for the student that you want to check the MAP score for,
    # return the index for that student, and then use that index to search the MAP list for their score.
    def check_map(self):
        student = input("Which student do you want to check the math MAP score of? ")
        student.strip()
        student.lower()
        if student in self.students[:]:
            student_num = self.students.index(student)
            print(student + "'s MAP score for math is " + self.MAP[student_num])
        else:
            print ("That student isn't in this class!")

    # This function will search the students list for the student that you want to check the grade level of,
    # return the index for that student, and then use that index to search the student grade list for their grade level.
    def check_student_grade(self):
        student = input("Which student do you want to check the grade level of? ")
        student.strip()
        student.lower()
        if student in self.students[:]:
            student_num = self.students.index(student)
            print(student + "'s grade level is " + self.student_grade[student_num])
        else:
            print ("That student isn't in this class!")

    #This function will take the average standards based grade and turn it into a traditional letter grade.
    def standard_to_letter(self):
        grade = float(input("What is the student's average standard grade? "))
        if grade <= 4.0 and grade >= 0.0:    
            if grade >= 3.65:
                print("This student has an A")
            elif grade >= 3.5:
                print("This student has an A-")
            elif grade >= 3.35:
                print("This student has a B+")
            elif grade >=3.15:
                print("This student has a B")
            elif grade >= 3:
                print("This student has a B-")
            elif grade >=2.85:
                print("This student has a C+")
            elif grade >=2.65:
                print("This student has a C")
            elif grade >=2.5:
                print("This student has a C-")
            elif grade >=2.35:
                print("This student has a D+")
            elif grade >=2.15:
                print("This student has a D")
            elif grade >=1.99:
                print("This student has a D-")
            else:
                print("This student failed the class")
        else:
            print("That's not a valid grade!")