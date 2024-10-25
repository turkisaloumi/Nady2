import os
import time
def clear_screen():
    os.system('cls'if os.name == 'nt' else 'clear')
class Nady:
    def __init__(self,first_name,last_name,emile,password,status = "inactive"):

        self.first_name = first_name
        self.last_name = last_name
        self.emile = emile
        self.password = password
        self.status = status
    def turki(self):
            print(f"first name : {self.first_name}")
            print(f"last name : {self.last_name}")
            print(f"emile : {self.emile}")
            print(f"password : {self.password}")
            print(f"status : {self.status}")
            print('_'*50)
def Add_new_user():    
    first_name = input("Enter first name : ")
    last_name = input("Enter last name : ")
    emile = input("Enter emile : ")
    password = input("enter password : ")
    return Nady(first_name,last_name,emile,password)
new_user = []
while True:
    print("\nwelcome to user management \n")
    print("\nChoice an action: \n")
    print("1. Add new user")
    print("2. Display all users")
    print("3. Exit\n")
    choice1 = input("Enter your choice : ")
    if choice1 == '1':
        clear_screen()
        new_user.append(Add_new_user())
        print("User added successfully!")
        time.sleep(2)
        clear_screen()
    elif choice1 == '2':
        clear_screen()
        if len(new_user) > 0 :
            print("Displaying all new_users .....")
            time.sleep(1)
            for i in new_user:
                i.turki()
        else :
            print("Sorry, didn't find any user to display!")
            time.sleep(2)
    elif choice1 == '3':
      clear_screen()
      print("Exiting ....")
      time.sleep(10000000)
    
        

