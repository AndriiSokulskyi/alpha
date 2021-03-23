from Class_user_New import User 

class Teacher(User):
  def __init__(self, subject):
    self.subject = subject

  def __str__(self):
    return f"Subject: {self.subject}"

  def __repr__(self):
    return f"Teacher({self.subject})"

  @property 
  def subject(self):
    return self._subject

  @subject.setter
  def subject(self, value):
    self._subject = value

