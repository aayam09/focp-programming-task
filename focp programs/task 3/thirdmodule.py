import getpass
import hashlib

def get_non_empty_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.strip():
            return user_input
        else:
            print("Input cannot be empty. Please try again.")


def get_secure_input(prompt):
    while True:
        password = getpass.getpass(prompt)
        if password.strip():
            return password
        else:
            print("Password cannot be empty. Please try again.")

def encrypt(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()
    
def write_file(file_path, lines):
    with open(file_path, "w") as file:
        file.writelines(lines)


