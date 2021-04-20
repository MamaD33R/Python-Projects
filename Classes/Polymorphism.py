


class SchoolPersons:        # Created parent class SchoolPersons
    Name = 'Mrs.Example'
    Address = 'Somewhere Ave.'
    School_ID = 3748
    Email = 'yesverynice@gmail.com '

    def Login(self):
        type_Name = input("Please enter your name: ")
        type_Email = input("Please enter your email: ")
        if (type_Email == self.Email and type_Name == self.Name):
            print("Thanks for signing in! Check out the latest school news updates, {}.".format(type_Name))
        else:
            print("We don't recognize this email..")

class Teacher(SchoolPersons): # Child class with the TeacherID instead of School_ID
    Pay = 15.00
    Phone = 234294211
    TeacherID = "200B2"

    def Login(self):
        type_TeacherID = input("Please enter your name: ")
        type_Email = input("Please enter your email: ")
        if (type_Email == self.Email and type_TeacherID == self.TeacherID):
            print("Thanks for signing in! More info on the meeting is available, {}.".format(type_name))
        else:
            print("We don't recognize this email or ID..")

class Student(SchoolPersons): # Child class with Student ID instead of normal school ID
    GPA = 3.5
    Grade = 11
    StudentID = 2002

    def Login(self):
        type_studentID = input("Please enter your student ID: ")
        type_email = input("Please enter your email: ")
        if (type_Email == self.Email and type_StudentID == self.StudentID):
            print("Thanks for signing in! Check out your recent grades or upcoming events, {}.".format(type_name))
        else:
            print("We don't recognize this email or ID..")


if __name__ == "__main__":  
    user = SchoolPersons()
    user.Login()

    # making use of the functions under each class to display the login entry
    teach = Teacher()
    teach.Login()


    stu = Student()
    stu.Login()
