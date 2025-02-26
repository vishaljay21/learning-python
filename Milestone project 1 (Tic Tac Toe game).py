"""
*** PROBLEM STATEMENT ***
- Build a Tic-Tac-Toe game
- It has to be played with the help of NumPad using numbers 1-9

     |     |            -> listb (blank list)
 (7) | (8) | (9)        -> list3
     |     |     
-----------------       -> listd (dash list)
     |     |    
 (4) | (5) | (6)        -> list2
     |     |     
-----------------
     |     |    
 (1) | (2) | (3)        -> list1
     |     |      

"""
class tictactoe:
    def __init__(self):
        
        print("\n*** WELCOME TO TIC-TAC-TOE GAME ***")
        
        # Initializations for blank board
        self.listb = [" "," "," ","|"," "," "," ","|"," "," "," "]          # un-useful row (blank list)
        self.temp_list3 = [" ","7"," ","|"," ","8"," ","|"," ","9"," "]     # useful row-1, imp index numbers: 1,5,9
        self.listd = ["---------------------"]                              # Horizontal line
        self.temp_list2 = [" ","4"," ","|"," ","5"," ","|"," ","6"," "]     # useful row-2
        self.temp_list1 = [" ","1"," ","|"," ","2"," ","|"," ","3"," "]     # useful row-3

        # Display instruction board
        print(*self.listb)
        print(*self.temp_list3)
        print(*self.listb)

        print(*self.listd)

        print(*self.listb)
        print(*self.temp_list2)
        print(*self.listb)

        print(*self.listd)

        print(*self.listb)
        print(*self.temp_list1)
        print(*self.listb)

        # Lists initialization for gameplay
        self.list3 = self.listb.copy()
        self.list2 = self.listb.copy()
        self.list1 = self.listb.copy()

        # Choosing 'X' or 'O' for Player-1
        while (True):                                                       # condition for input validation
            self.p1 = input("\nChoose 'X' or 'O' for Player-1: ")             
            if self.p1 == "X":                                              
                self.p2 = "O"
                break
            elif self.p1 == "O":
                self.p2 = "X"
                break
            else:
                print("Please choose a valid character")

        print(f"\n[Player-1 ({self.p1}) ; Player-2 ({self.p2})]\n")

        self.p1_flag = 0                                                    # Flag variable for Player-1
        self.p2_flag = 0                                                    # Flag variable for Player-2
        
        self.i = 0                                                          # Iterator to check if the game is drawn
    
    def game_begin(self):
        # Display blank board before game begins
        print(*self.listb)
        print(*self.list3)
        print(*self.listb)

        print(*self.listd)

        print(*self.listb)
        print(*self.list2)
        print(*self.listb)

        print(*self.listd)

        print(*self.listb)
        print(*self.list1)
        print(*self.listb)

        while (self.i<9):                                                   # Max 9 entries possible
            # Player-1's turn
            self.p1t = int(input(f"Player-1 ({self.p1}) turn: "))

            # Input Mapping for Player-1
            if self.p1t == 1:
                self.list1[1] = self.p1
            elif self.p1t == 2:
                self.list1[5] = self.p1
            elif self.p1t == 3:
                self.list1[9] = self.p1
            elif self.p1t == 4:
                self.list2[1] = self.p1
            elif self.p1t == 5:
                self.list2[5] = self.p1
            elif self.p1t == 6:
                self.list2[9] = self.p1
            elif self.p1t == 7:
                self.list3[1] = self.p1
            elif self.p1t == 8:
                self.list3[5] = self.p1
            elif self.p1t == 9:
                self.list3[9] = self.p1

            # Display current board status
            print(*self.listb)
            print(*self.list3)
            print(*self.listb)

            print(*self.listd)

            print(*self.listb)
            print(*self.list2)
            print(*self.listb)

            print(*self.listd)

            print(*self.listb)
            print(*self.list1)
            print(*self.listb)
            
            #check if Player-1 won
            if (self.list3[1] == self.list3[5] == self.list3[9] == self.p1) or (self.list2[1] == self.list2[5] == self.list2[9] == self.p1) or (self.list1[1] == self.list1[5] == self.list1[9] == self.p1):
                print("Congratulations, Player-1 Won :)")
                self.p1_flag = 1
                break
            elif (self.list3[1] == self.list2[1] == self.list1[1] == self.p1) or (self.list3[5] == self.list2[5] == self.list1[5] == self.p1) or (self.list3[9] == self.list2[9] == self.list1[9] == self.p1):
                print("Congratulations, Player-1 Won :)")
                self.p1_flag = 1
                break
            elif (self.list3[1] == self.list2[5] == self.list1[9] == self.p1) or (self.list3[9] == self.list2[5] == self.list1[1] == self.p1):
                print("Congratulations, Player-1 Won :)")
                self.p1_flag = 1
                break
            
            self.i += 1
            if self.i == 9:                                                 # To check if the 9th entry is done
                break
            
            # Player-2's turn
            self.p2t = int(input(f"Player-2 ({self.p2}) turn: "))

            # Input Mapping for Player-2
            if self.p2t == 1:
                self.list1[1] = self.p2
            elif self.p2t == 2:
                self.list1[5] = self.p2
            elif self.p2t == 3:
                self.list1[9] = self.p2
            elif self.p2t == 4:
                self.list2[1] = self.p2
            elif self.p2t == 5:
                self.list2[5] = self.p2
            elif self.p2t == 6:
                self.list2[9] = self.p2
            elif self.p2t == 7:
                self.list3[1] = self.p2
            elif self.p2t == 8:
                self.list3[5] = self.p2
            elif self.p2t == 9:
                self.list3[9] = self.p2

            # Display current board status
            print(*self.listb)
            print(*self.list3)
            print(*self.listb)

            print(*self.listd)

            print(*self.listb)
            print(*self.list2)
            print(*self.listb)

            print(*self.listd)

            print(*self.listb)
            print(*self.list1)
            print(*self.listb)

            #check if Player-2 won
            if (self.list3[1] == self.list3[5] == self.list3[9] == self.p2) or (self.list2[1] == self.list2[5] == self.list2[9] == self.p2) or (self.list1[1] == self.list1[5] == self.list1[9] == self.p2):
                print("Congratulations, Player-2 Won :)")
                self.p2_flag = 1
                break
            elif (self.list3[1] == self.list2[1] == self.list1[1] == self.p2) or (self.list3[5] == self.list2[5] == self.list1[5] == self.p2) or (self.list3[9] == self.list2[9] == self.list1[9] == self.p2):
                print("Congratulations, Player-2 Won :)")
                self.p2_flag = 1
                break
            elif (self.list3[1] == self.list2[5] == self.list1[9] == self.p2) or (self.list3[9] == self.list2[5] == self.list1[1] == self.p2):
                print("Congratulations, Player-2 Won :)")
                self.p2_flag = 1
                break

            self.i += 1
        
        # To check if the game is drawn
        if (self.p1_flag == 0) and (self.p2_flag == 0):
            print("Game Draw")

play = tictactoe()
play.game_begin()

# For replay
choice = input("Replay (Y or N): ")
while 1:                                                                    # condition for input validation
    if choice == "Y":
        play.__init__()
        play.game_begin()
        choice = input("Replay (Y or N): ")
    elif choice == "N":
        print("Thank You playing :)")
        break
    else:
        print("Invalid response :/")
        choice = input("Replay (Y or N): ")


                
        
        
        

  








