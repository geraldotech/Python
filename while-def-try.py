def print_menu():
    print("1 - option one")
    print("2 - option two")


def option1():
     print('Handle option \'Option 1\'')

while(True):
    print_menu()
    option = ""
    try:
        option = int(input("Enter choice: "))
    except:
        print('Wrong input. Please enter a number ...')  
    if option == 1:        
        print("escolheu um")
    elif option == 2:    
        option1()
    elif option == 0:    
        exit() 
    else:      
         print('Invalid option. Please enter a number between 1')
