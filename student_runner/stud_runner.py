from student_package.student_type import Student

Student.school_name = "Global school"
Student.school_address = "Chennai"

student1 = Student(1001,"jack","jack@gmail.com",45.2)
student2 = Student(1002,"peter","peter@gmail.com",85.2)
student3= Student(1003,"mark","mark@gmail.com",56.5)

res = student1.get_name_with_percentage()
print(res)