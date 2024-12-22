class Father:
    def __init__(self, father_name):
        self.father_name = father_name


class Mother:
    def __init__(self, mother_name):
        self.mother_name = mother_name


class child(Father, Mother):
    def __init__(self, name, father_name, mother_name):
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)
        self.name = name

    def display(self):
        print("My name is ", self.name)
        print("My father name is ", self.father_name)
        print("My Mother name is ", self.mother_name)

instance = child("ram", "father", "mother")

instance.display()