from datetime import datetime
class user():
    def __init__(self, id, password, name,roles= None, classes= None , started_at=datetime.now()):
        self.name = name
        self.id = id
        self.__pasword = password
        self.roles = roles or []
        self.classes = classes or []
        self.started_at = started_at




    def email(self):
        return (f"{self.id}@tafe.wa.etc")

    def login(self, entered_pasword):
        if entered_pasword == self.__pasword:
            return "Cookie time!"
        else:
            return "Try again!"

mark = user("404","1234", "Mark")
print(mark.email())





class User:

    NEXT_USER_ID = 1



    def __init__(self, name, password, roles= None, classes= None , started_at=datetime.now()):

        self.id = self.NEXT_USER_ID

        User.NEXT_USER_ID += 1

        self.name = name

        self.email = f"{self.id }@tafe.wa.edu.au"

        self.password = "This really should be a salted hash"

        self.roles = roles or []

        self.classes = classes or []

        self.started_at = started_at

    

    def enrol_to_class(self, class_name):

        if class_name in self.classes:

            print(f"{self.name} - {self.id} is already enrolled in {class_name}")

        else:

            self.classes.append(class_name)



    def unenrol_from_class(self, class_name):

        if class_name in self.classes:

            self.classes.remove(class_name)

        else:

            print(f"{self.name} - {self.id} is not enrolled in {class_name}")