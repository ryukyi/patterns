class Model:
    def __init__(self):
        self.data = "Initial Data"

    def update_data(self, new_data):
        self.data = new_data
        print(f"Model updated to: {self.data}")

class View:
    def display(self, data):
        print(f"View is displaying: {data}")

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_model(self, data):
        self.model.update_data(data)

    def refresh_view(self):
        self.view.display(self.model.data)

if __name__ == "__main__":
    model = Model()
    view = View()
    controller = Controller(model, view)

    controller.update_model("Updated Data")
    controller.refresh_view()
