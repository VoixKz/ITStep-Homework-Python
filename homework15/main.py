class MainClass:
    def __init__(self, text=None):
        self.text = text

    def set_text(self, text=None):
        if text is not None:
            self.text = text
        else:
            self.text = input("Enter text: ")

    def get_text(self):
        return self.text

    def display(self):
        print(f"Text: {self.text}")


class ChildClass(MainClass):
    def __init__(self, text=None, number=None):
        super().__init__(text)
        self.number = number

    def set_number(self, number=None):
        if number is not None:
            self.number = number
        else:
            try:
                self.number = float(input("Enter number: "))
            except ValueError:
                print("Invalid type. Please enter a number")

    def get_number(self):
        return self.number

    def display(self):
        super().display()
        print(f"Number: {self.number}")

main_obj = MainClass()
main_obj.set_text("Halo-o!")
main_obj.set_text()
main_obj.display()
child_obj = ChildClass()
child_obj.set_text("Halo-o my child!")
child_obj.set_text()
child_obj.set_number(1337.228007993)
child_obj.set_number()
child_obj.display()