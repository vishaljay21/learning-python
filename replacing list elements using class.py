"""
*** PROBLEM STATEMENT ***
Make a list and display it to user
Ask the user for a new string that is to be inserted and the corresponding position number
(reask the position number in case of an invalid input)
Replace the said element in the list, and display the new list
Again ask whether to insert a new string? (Yes or No)

"""
default_list = [1,2,3,4]

print("Original List: ", default_list)
resp = "Y"

class list_fun:
    def __init__(self):
        self.new_list = default_list.copy()

    def ask(self):
        self.element = input("Enter the string to be inserted: ")
    
    def check(self):
        while (True):
            self.pos_no = input("Enter position no. (1-4): ")
            if self.pos_no.isdigit() == False:
                print("Not a number :/")
            elif int(self.pos_no) not in range(1,5):
                print("Out of range position no. :/")
            else:
                break

    def process(self):
        self.new_list[int(self.pos_no) - 1] = self.element

    def display(self):
        print("Here is the current list:\n", self.new_list)
        global resp
        resp = input("\nDo you want to enter another string? (Y or N): ")


c1 = list_fun()

while (True):

    if resp == "Y":
        c1.ask()
        c1.check()
        c1.process()
        c1.display()
    elif resp == "N":
        print("Thank you :)")
        break

    else:
        print("Invalid response :/")
        resp = input("\nDo you want to enter another string? (Y or N): ")