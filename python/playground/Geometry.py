import GeoClass

Geo1Students = None
Geo2Students = None
Geo3Students = None
Geo4Students = None
Geo1Grades = None
Geo2Grades = None
Geo3Grades = None
Geo4Grades = None
Geo1MAP = None
Geo2MAP = None
Geo3MAP = None
Geo4MAP = None
Geo1Student_grade = None
Geo2Student_grade = None
Geo3Student_grade = None
Geo4Student_grade = None

with open('Geo1.txt', 'r') as students1:
    Geo1Students = students1.readlines().copy()

with open('Geo2.txt', 'r') as students2:
    Geo2Students = students2.readlines().copy()

with open('Geo3.txt', 'r') as students3:
    Geo3Students = students3.readlines().copy()

with open('Geo4.txt', 'r') as students4:
    Geo4Students = students4.readlines().copy()

with open('Geo1.txt', 'r') as grades1:
    Geo1Grades = grades1.readlines().copy()

with open('Geo2.txt', 'r') as grades2:
    Geo2Grades = grades2.readlines().copy()

with open('Geo3.txt', 'r') as grades3:
    Geo3Grades = grades3.readlines().copy()

with open('Geo4.txt', 'r') as grades4:
    Geo4Grades = grades4.readlines().copy()

with open('Geo1.txt', 'r') as MAP1:
    Geo1MAP = MAP1.readlines().copy()

with open('Geo2.txt', 'r') as MAP2:
    Geo2MAP = MAP2.readlines().copy()

with open('Geo3.txt', 'r') as MAP3:
    Geo3MAP = MAP3.readlines().copy()

with open('Geo4.txt', 'r') as MAP4:
    Geo4MAP = MAP4.readlines().copy()

with open('Geo1.txt', 'r') as student_grade1:
    Geo1Student_grade = student_grade1.readlines().copy()

with open('Geo2.txt', 'r') as student_grade2:
    Geo2Student_grade = student_grade2.readlines().copy()

with open('Geo3.txt', 'r') as student_grade3:
    Geo3Student_grade = student_grade3.readlines().copy()

with open('Geo4.txt', 'r') as student_grade4:
    Geo4Student_grade = student_grade4.readlines().copy()

Geo1 = GeoClass.Geometry(Geo1Students, Geo1Grades, Geo1MAP, Geo1Student_grade)
Geo2 = GeoClass.Geometry(Geo2Students, Geo2Grades, Geo2MAP, Geo2Student_grade)
Geo3 = GeoClass.Geometry(Geo3Students, Geo3Grades, Geo3MAP, Geo3Student_grade)
Geo4 = GeoClass.Geometry(Geo4Students, Geo4Grades, Geo4MAP, Geo4Student_grade)

print("Welcome to the Geometry Help Program!")
while True:
    print("What would you like to do?")
    print("Grades - Check Student Grades")
    print("MAP - Check Student MAP Scores for Math")
    print("Level - Check Student Grade Level")
    print("Exit - Exit the program")
    choice = input()
    choice = choice.lower().strip()
    if choice == "grades":
        while True:
            geoclass = int(input("What class do you want to check? "))
            if geoclass == 1:
                Geo1.check_grade()
                break
            elif geoclass == 2:
                Geo2.check_grade()
                break
            elif geoclass == 3:
                Geo3.check_grade()
                break
            elif geoclass == 4:
                Geo4.check_grade()
                break
            else:
                print("That isn't a class you have! Choose an hour")
    elif choice == "map":
        while True:
            geoclass = int(input("What class do you want to check? "))
            if geoclass == 1:
                Geo1.check_map()
                break
            elif geoclass == 2:
                Geo2.check_map()
                break
            elif geoclass == 3:
                Geo3.check_map()
                break
            elif geoclass == 4:
                Geo4.check_map()
                break
            else:
                print("That isn't a class you have! Choose an hour")
    elif choice == "level":
        while True:
            geoclass = int(input("What class do you want to check? "))
            if geoclass == 1:
                Geo1.check_student_grade()
                break
            elif geoclass == 2:
                Geo2.check_student_grade()
                break
            elif geoclass == 3:
                Geo3.check_student_grade()
                break
            elif geoclass == 4:
                Geo4.check_student_grade()
                break
            else:
                print("That isn't a class you have! Choose an hour")
    elif choice == "exit":
        break
    else:
        print("That isn't a valid option.")

print("Thank you for using the Geometry Help Program!")