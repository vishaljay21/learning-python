"""
*** PROBLEM STATEMENT ***
Make a list and display it to user
Ask the user for a new string that is to be inserted and the corresponding valid position
(reask the position number in case of an invalid input)
Replace the said element in the list, and display the new list
Again ask whether to insert a new string? (Yes or no)

"""
default_list = [1,2,3,4]
new_list = default_list.copy()

def ask():
    element = input("Enter the string to be inserted: ")
    while (True):
        pos_no = input("Enter position no. (1-4): ")
        if pos_no.isdigit() == False:
            print("Not a number :/")
        elif int(pos_no) not in range(1,5):
            print("Out of range position no. :/")
        else:
            break

    new_list[int(pos_no) - 1] = element

    print("Here is the current list:\n", new_list)
    global resp
    resp = input("\nDo you want to enter another string? (Y or N): ")

print("Original List: ", default_list)

resp = "Y"

while (True):

    if resp == "Y":
        ask()
    elif resp == "N":
        print("Thank you :)")
        break

    else:
        print("Invalid response :/")
        resp = input("\nDo you want to enter another string? (Y or N): ")
