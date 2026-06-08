#Course Enrollment Verification
course_students = ["Vaishnu", "Krushnali", "Nishi", "Ankita"]

name = input("Enter student name: ")

if name in course_students:
    print("Student is enrolled in the course")
else:
    print("Student is not enrolled in the course")