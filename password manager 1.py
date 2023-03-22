#password manager
passwords = {}

def add_password(account, password) :
    passwords[account] = password
    
def get_password(account):
    return passwords.get(account, None)

def main():
    while True:
        print("1. Add Password")
        print("2. Get Password")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            account = input("Enter Account Name: ")
            password = input("Enter Password: ")
            add_password(account, password)
        elif choice == "2":
            account = input("Enter Account Name: ")
            password = get_password(account)
            if password:
                print(f"Password for {account}: {password}")
            else:
                print(f"No Password found for {account}")
        elif choice == "3":
            break
        else:
            print("Invalid Choice")
if __name__ == "__main__":
    main()

                
