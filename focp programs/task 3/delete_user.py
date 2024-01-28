import thirdmodule

def delete_user(file_path, deleted_user, hashed_password):
    """
    Deletes a user from a file if the provided user and hashed password match.

    Args:
        file_path (str): Path to the file containing user information.
        deleted_user (str): The user to be deleted.
        hashed_password (str): The hashed password for verification.

    Raises:
        FileNotFoundError: If the specified file is not found.
        PermissionError: If there is a permission issue while accessing the file.
    """
    try:
        modified_lines = []
        lines = thirdmodule.read_file(file_path)
        
        user_found = False  

        for line in lines:
            values = line.strip().split(":")
            user, real_name, password = values

            if user == deleted_user and password == hashed_password:
                user_found = True
            else:
                modified_lines.append(f"{user}:{real_name}:{password}\n")

        if user_found:
            print(f"User {deleted_user} has been successfully deleted.")
        else:
            print("No changes were made.")

        thirdmodule.write_file(file_path, modified_lines)
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission issue while accessing the file.")

def main():
    """
    Main function to execute user deletion process.
    """
    try:
        deleted_user = thirdmodule.get_non_empty_input("Enter the user to be deleted: ")
        deleted_password = thirdmodule.get_secure_input("Enter the password: ")

        hashed_password = thirdmodule.encrypt(deleted_password)

        file_path = "third.txt"
        delete_user(file_path, deleted_user, hashed_password)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
