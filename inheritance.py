# Inheritance allows you to pass in an existing class (i.e. parent class), 
# into a new class (i.e. child class)

# PURPOSE: allows programmers to REUSE & BUILD upon exisiting classes 
# E.g passing in the parent class allows the child class access to the 
#     init, attributes & methods within the parent class

class Person:
    def __init__(self, first_name, sur_name):
        self.first_name = first_name
        self.sur_name = sur_name

    def greeting(self):
        return f"Hello my name is {self.first_name}, nice to meet you."
    
    def introduction(self):
        return f"I am {self.first_name} {self.sur_name}"
    

class Agent(Person):
    # To add more attributes than what was provide by the parent class you need to 
    # override the init method itself, and pass in your desired parameters in the child class

    def __init__(self, first_name, sur_name, code_name):
        Person.__init__(self, first_name, sur_name)
        self.code_name = code_name
    
    # If you want to override an inherited method you can redefine it
    def introduction(self):
        return f"I am agent 001, agent {self.code_name}."

    def reveal(self, passcode):
        if passcode == 123:
            return f"{self.first_name} is a an agent!"
        else:
            # calls method inherited from Person class
            self.introduction()


a1 = Agent("John", "Smith", "Mr. A")
print(a1.introduction())
print(a1.reveal(123))

