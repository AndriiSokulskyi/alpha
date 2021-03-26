from datetime import datetime
#from Class_user.py import User
#from Schedule_organize_for_student import schedule
from Class_user_New import User

class Student(User):
    def __init__(self, name, surname, fathers_name, b_date, email, password, photo, city, schedule, signal, ID, clase):
        User.__init__(self, name, surname, fathers_name, b_date, email, password, photo, city, schedule, signal, ID)
        self.clase = clase

    def __str__(self):
        User.__str__(self)
        to_return = f"email : {self.email}\n " \
                    f"name : {self.name}\nsurname : {self.surname}\n" \
                    f"fathers_name : {self.fathers_name}\nbirthday : {self.b_date}\n" \
                    f"photo : {self.photo}\ncity : {self.city}\nschedule : {self.schedule} \n" \
                    f"signal : {self.signal}\n class : {self.clase} " 
        return to_return 

    def __repr__(self):
        return f"User({self.ID},{self.email},{self.password},{self.surname},{self.name},{self.fathers_name}," \
               f"{self.photo},{self.b_date},{self.city},{self.schedule},{self.signal})\n Learn in ({self.clase})\n"

    @property
    def clase(self):
        return self._clase

    @clase.setter
    def clase(self, value):
        self._clase = value

    
