from Class_user_New import Lesson, User 
#from enum import Enum // потрібні дані для валідації

#Week = Enum("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

Math = Lesson("attantions", "marks", "homework")
Bio=Lesson("attantions2", "marks2", "homework2")
Sport =Lesson("attantions2", "marks24", "homework2")

Monday = {"1" : Math,
        "2" : Sport, 
        "3" : Bio}
Tuesday = {"1" : Math,
        "2" : Bio, 
        "3" : Sport}
Wednesday = {"1" : Math,
            "2" : Bio, 
            "3" : Math}

schedule = (Monday, Tuesday, Wednesday)

#перевірка 
for it in schedule:
    print(it)

user1 = User("name", "surname", "fathers_name", "10-5-1999", "email", "password", "photo", "city", str(schedule), False, ID=0)

print (user1)