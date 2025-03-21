import random
import string


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("The number cannot be negative. Please enter a positive number.\n")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.\n")


def password_gen():

    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase
    numbers = string.digits
    symbols = "!@#$%&*()-_=+"  # safe symbols

    while True:
        print("  _____________________________________________\n")
        print("\n\t*** 🔑🔑🔑 Password Generator 🔑🔑🔑 ***\n")
        print("The password can consist of upper and lower case letters, numbers, and symbols.")
        print("The minimum length is 8 and the maximum is 100 characters.\n")
        try:
            total = 0
            print("########################################################################")
            num_upper_letters = get_positive_integer("🗝️ Enter the number of uppercase letters: ")
            num_lower_letters = get_positive_integer("🗝️ Enter the number of lowercase letters: ")
            num_numbers = get_positive_integer("🗝️ Enter the number of digits: ")
            num_symbols = get_positive_integer("🗝️ Enter the number of symbols: ")

            total = num_upper_letters + num_lower_letters + num_numbers + num_symbols
            if total == 0:
                print("\nThe password cannot be empty. Press any key to continue, 'q' to exit.")
                if input().lower() == 'q':
                    break
                continue
            elif total < 8:
                print("\nThe minimum length is 8 characters. Press any key to continue, 'q' to exit.")
                if input().lower() == 'q':
                    break
                continue
            elif total > 100:
                print("\nThe maximum length is 100 characters. Press any key to continue, 'q' to exit.")
                if input().lower() == 'q':
                    break
                continue

        except ValueError:
            print("\nInvalid input. Please enter integers only. Press any key to continue, 'q' to exit.")
            if input().lower() == 'q':
                break
            continue

        passwd_arr = []

        for _ in range(num_upper_letters):
            passwd_arr.append(random.choice(upper_letters))
        for _ in range(num_lower_letters):
            passwd_arr.append(random.choice(lower_letters))
        for _ in range(num_numbers):
            passwd_arr.append(random.choice(numbers))
        for _ in range(num_symbols):
            passwd_arr.append(random.choice(symbols))

        random.shuffle(passwd_arr)
        password = ''.join(passwd_arr)

        print(f"\n🍀🍀🍀 Password generated successfully: {password}")
        break


while True:
    password_gen()
    print("\nPress any key to continue, 'q' to exit.\n")
    if input().lower() == 'q':
        break
