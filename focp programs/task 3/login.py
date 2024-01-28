import thirdmodule

def main():
    """
    Main function to handle user login.
    """
    try:
        login_username = thirdmodule.get_non_empty_input("Enter username: ")
        login_password = thirdmodule.get_secure_input("Enter password: ")
        hashed_password = thirdmodule.encrypt(login_password)
        
        file_path = "third.txt"
        login_user(file_path, login_username, hashed_password)
    except Exception as e:
        print(f"An error occurred: {e}")

def login_user(file_path, login_username, hashed_password):
    """
    Validates user credentials against a file.

    Args:
        file_path (str): Path to the file containing user information.
        login_username (str): User-entered username for login.
        hashed_password (str): Hashed password for login.

    Prints:
        "Access granted" if login is successful, otherwise "Access denied".
    """
    try:
        lines = thirdmodule.read_file(file_path)
        
        for line in lines:
            values = line.strip().split(":")
            user, real_name, password = values
            
            if login_username == user and hashed_password == password:
                print("Access granted")
                return

        print("Access denied")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission issue while accessing the file.")

if __name__ == "__main__":
    main()
