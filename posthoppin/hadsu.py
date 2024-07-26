class Hadsu:
        def __init__(self, first_name, last_name):
            self.fname = first_name
            self.lname = last_name
        
        def Print(self):
            print(f"Hello Mr/Ms. {self.lname}. Welcome to Typer {self.fname}")