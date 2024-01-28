import thirdmodule


def is_duplicate_user(user):
    """
    Check if a given username already exists in the user data file.

    Parameters:
    - user (str): The username to check.

    Returns:
    - bool: True if the username already exists, False otherwise.
    """
    try:
        with open("third.txt", "r") as file:
            for line in file.readlines():
                values = line.strip().split(":")
                if user == values[0]:
                    return True
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission issue while accessing the file.")
    return False


def add_user_to_file(user, real_name, hashed_password):
    """
    Add a new user to the user data file.

    Parameters:
    - user (str): The username of the new user.
    - real_name (str): The real name of the new user.
    - hashed_password (str): The hashed password of the new user.
    """
    try:
        with open("third.txt", "a") as file:
            file.write(f"{user}:{real_name}:{hashed_password}\n")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission issue while accessing the file.")


def main():
    """
    Main function to execute user creation process.
    """
    try:
        while True:
            user = thirdmodule.get_non_empty_input("Enter username: ")
            
            if is_duplicate_user(user):
                print("Username already exists. Please choose a different username.")
            else:
                break  # Break out of the loop if the username is not a duplicate

        real_name = thirdmodule.get_non_empty_input("Enter real name: ")
        password = thirdmodule.get_secure_input("Enter password: ")
        hashed_password = thirdmodule.encrypt(password)
        
        add_user_to_file(user, real_name, hashed_password)
        print("User created successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
