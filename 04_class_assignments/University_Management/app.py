class User():
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login(self):
        print("Login User")

    def logout(self):
        print("Logout User")

user = User("hammad" , "2333")
user.login()
    


class Admin(User):
  def __init__(self , email , password):
    super().__init__(email , password)

  def login(self , admin_key):
    if not admin_key == "1234":
       print("Invalid Key")
    else:
       print("Admin Login")


admin1 = Admin("hammad" , "2333")
admin1.login("555")

admin2  = Admin("Hamzah" , "2333")
admin2.login("1234")

class Person():
  def __init__(self, my_name, my_age) -> None:
    self.name = my_name
    self.age  = my_age

  def get_details(self):
    print( self.name, self.age )


class Student(Person):
  def __init__(self, name, age, roll_number) -> None:
    super().__init__(name, age)
    self.roll_number:str = roll_number
    self.courses = []

  def register_for_course(self, course):
    self.courses.append( course )

s1 = Student("Ali", 22, "GIAIC123")

class Course():
  def __init__(self, course_id, name):
    self.id = course_id
    self.name = name

ai_course = Course( 1, "Agentic AI" )

s1.register_for_course( ai_course )