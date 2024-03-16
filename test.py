import hashlib
import os

def detect_hash_algorithm(hash_value):
    hash_length = len(hash_value)

    if hash_length == 32:
        return 'MD5'
    elif hash_length == 40:
        return 'SHA1'
    elif hash_length == 64:
        return 'SHA256'
    elif hash_length == 96:
        return 'SHA384'
    elif hash_length == 128:
        return 'SHA512'
    else:
        return 'Unknown Algorithm'

def encode_password(password, algorithm):
    if algorithm == 'MD5':
        encoded = hashlib.md5(password.encode()).hexdigest()
    elif algorithm == 'SHA-1':
        encoded = hashlib.sha1(password.encode()).hexdigest()
    elif algorithm == 'SHA-256':
        encoded = hashlib.sha256(password.encode()).hexdigest()
    elif algorithm == 'SHA-512':
        encoded = hashlib.sha512(password.encode()).hexdigest()
    else:
        encoded = 'Invalid algorithm'

    return encoded

def save_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content + '\n')

if __name__ == '__main__':
    while True:  # Loop indefinitely
        print("\033[1;36mWelcome to Password Hashing and Algorithm Detection Tool!\033[0m")
        print("This program is designed by iamroyalmayor Spectrum Solutions.")
        print("Please use this program ethically and responsibly.")  
        print("1. Detect Hash Algorithm")
        print("2. Encode Password")
        print("3. Exit")

        print("other modules will be added very soon")
        choice = input("\033[1;33mEnter your choice (1, 2, or 3 ):\033[0m ")

        if choice == '3':
            break  # Exit the loop if the user chooses to exit

        if choice.lower() == 'exit':
            break  # Exit the loop if the user chooses to quit

        if choice == '1':
            hash_input = input("Enter the password hash value: ")
            algorithm_type = detect_hash_algorithm(hash_input)
            print(f"\033[1;32mThe password was encoded using the {algorithm_type} algorithm.\033[0m")

            # Save to file
            save_to_file('hash_output.txt', f"hash value = {hash_input}   algorithm = {algorithm_type}")
        elif choice == '2':
            password = input("Enter the password to encode: ")
            print("Choose the algorithm to use:")
            print("1. MD5")
            print("2. SHA-1")
            print("3. SHA-256")
            print("4. SHA-512")
            algorithm_choice = input("Enter your choice (1-4): ")

            algorithms = {1: 'MD5', 2: 'SHA-1', 3: 'SHA-256', 4: 'SHA-512'}
            algorithm = algorithms.get(int(algorithm_choice), None)

            if algorithm:
                encoded_password = encode_password(password, algorithm)
                print(f"\033[1;32mThe encoded password using {algorithm} algorithm is: {encoded_password}\033[0m")
                print("\033[1;35mEncoded password and hash value saved successfully.\033[0m")

                # Save to file
                save_to_file('encoded_passwords.txt', f"Password = {password} hash = {encoded_password}")
            else:
                print("\033[1;31mInvalid algorithm choice.\033[0m")
        else:
            print("\033[1;31mInvalid choice. Please enter 1, 2, or 'exit'.\033[0m")
