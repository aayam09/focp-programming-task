import thirdmodule

def main():
    """
    Main function to initiate the process of changing a user's password.
    """
    try:
        changed_user = thirdmodule.get_non_empty_input("Enter the user to be changed: ")
        changed_password = thirdmodule.get_secure_input("Enter the current password: ")

        hashed_password = thirdmodule.encrypt(changed_password)

        file_path = "third.txt"

        change_password(changed_user, hashed_password, file_path)

    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission issue while accessing the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def change_password(changed_user, hashed_password, file_path):
    """
    Change the password for a specified user in a file.

    Args:
        changed_user (str): The user for whom the password needs to be changed.
        hashed_password (str): The hashed current password for verification.
        file_path (str): Path to the file containing user information.

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

            if user == changed_user and hashed_password == password:
                new_password = thirdmodule.get_secure_input("Enter the new password: ")
                confirm_password = thirdmodule.get_secure_input("Confirm the new password: ")

                if new_password == confirm_password:
                    new_password_encrypted = thirdmodule.encrypt(new_password)
                    modified_lines.append(f"{user}:{real_name}:{new_password_encrypted}\n")
                    user_found = True
                else:
                    print("Passwords do not match. Password change aborted.")
                    return
            else:
                modified_lines.append(f"{user}:{real_name}:{password}\n")

        if user_found:
            print(f"Password for user '{changed_user}' has been successfully changed.")
            thirdmodule.write_file(file_path, modified_lines)
        else:
            print(f"User '{changed_user}' not found or password does not match. Password change aborted.")

    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission issue while accessing the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
