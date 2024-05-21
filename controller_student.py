class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_roll_no(self, roll_no):
        self.roll_no = roll_no

    def get_roll_no(self):
        return self.roll_no

class StudentView:
    def print_student_details(self, student_name, student_roll_no):
        print(f"Student: {student_name}, Roll No: {student_roll_no}")

class StudentController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def set_student_name(self, name):
        self.model.set_name(name)

    def get_student_name(self):
        return self.model.get_name()

    def set_student_roll_no(self, roll_no):
        self.model.set_roll_no(roll_no)

    def get_student_roll_no(self):
        return self.model.get_roll_no()

    def update_view(self):
        self.view.print_student_details(self.model.get_name(), self.model.get_roll_no())

if __name__ == "__main__":
    model = Student("John Doe", "1234")
    view = StudentView()
    controller = StudentController(model, view)

    controller.update_view()
    controller.set_student_name("Different Doe")
    controller.update_view()
