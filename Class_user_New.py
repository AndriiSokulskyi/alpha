from datetime import datetime 

class Lesson:
    def __init__(self, attentions, marks, homework):
        self.attentions = attentions
        self.marks = marks
        self.homework = homework

    def __str__(self):
        print(f"{self.marks} \n {self.homework} \n {self.attentions}")

    def __repr__(self):
        return f"Lessons({self.attentions}, {self.marks}, {self.homework})\n"

    @property
    def attentions(self):
        return self._attentions

    @attentions.setter
    def attentions(self, value):
        self._attentions = value
    
    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        self._marks = value

    @property
    def homework(self):
        return self._homework

    @homework.setter
    def homework(self, value):
        self._homework = value

class User:
    def __init__(self, name, surname, fathers_name, b_date, email, password, photo, city, schedule, signal, ID=0):
        self.name = name
        self.surname = surname
        self.fathers_name = fathers_name
        self.b_date = datetime.strptime(b_date, "%d-%m-%Y").date()
        self.email = email
        self.password = password 
        self.photo = photo
        self.city = city
        self.schedule = schedule
        self.signal = bool(signal)
        self.ID = id(self)

    def __str__(self):
        to_return = f"email : {self.email}\n " \
                    f"name : {self.name}\nsurname : {self.surname}\n" \
                    f"fathers_name : {self.fathers_name}\nbirthday : {self.b_date}\n" \
                    f"photo : {self.photo}\ncity : {self.city}\nschedule : {self.schedule} \n" \
                    f"signal : {self.signal}\n"
        return to_return

    def __repr__(self):
        return f"User({self.ID},{self.email},{self.password},{self.surname},{self.name},{self.fathers_name}," \
               f"{self.photo},{self.b_date},{self.city},{self.schedule},{self.signal})\n"

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, value):
        self._ID = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def fathers_name(self):
        return self._fathers_name

    @fathers_name.setter
    def fathers_name(self, value):
        self._fathers_name = value

    @property
    def photo(self):
        return self._photo

    @photo.setter
    def photo(self, value):
        self._photo = value

    @property
    def b_date(self):
        return self._b_date

    @b_date.setter
    def b_date(self, value):
        self._b_date = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def schedule(self):
        return self._schedule

    @schedule.setter
    def schedule(self, value):
        self._schedule = value

    @property
    def signal(self):
        return self._signal

    @signal.setter
    def signal(self, value):
        self._signal = value


