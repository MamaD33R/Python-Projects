

class SchoolPersons:        # Created parent class SchoolPersons
    Name = 'Mrs.Example'
    Address = 'Somewhere Ave.'
    School_ID = 3748
    Email = 'yesverynice@gmail.com '

class Teacher(SchoolPersons): # Child class with added attributes: pay, phone
    Pay = 15.00
    Phone = 234294211

class Student(SchoolPersons): # Child class with added attributes: gpa, grade
    GPA = 3.5
    Grade = 11
    
    
    
    
    
