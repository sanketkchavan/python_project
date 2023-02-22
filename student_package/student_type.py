
class Student:
    school_name = None
    school_address = None

    def __init__(self, student_id, student_name=None, student_mail_id=None, student_percentage=None):
        self.student_id = student_id
        self.student_name = student_name
        self.student_mail_id = student_mail_id
        self.student_percentage = student_percentage

    def get_name_with_percentage(self):
        return "Hi "+ self.student_name + " - Your Percentage is " + str(self.student_percentage)

    @property
    def get_student_name(self):
        return self.student_name

    @staticmethod
    def get_school_details():
        


