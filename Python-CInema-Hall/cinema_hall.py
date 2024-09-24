# Author: https://it-runner.pl
# MIT-licensed script.

print("\n\n*** DESIGN YOUR CINEMA HALL ***")


def cinema():
    try:
        # specify number of rows:
        rows = int(input("\nEnter the number of rows: \n"))
        while rows > 60 or rows < 4:
            print(("The number of rows must be between 4 and 60."))
            rows = int(input("\nEnter the number of rows: \n"))

        # specify number of seats in each row:
        seats = int(input("\nEnter the number of seats: \n"))
        while seats > 50 or seats < 10:
            print("The number of seats must be between 10 and 50.")
            seats = int(input("\nEnter the number of seats: \n"))

        # select seat numbering direction (vice versa):
        direction = input(
            "\nAre seats to be numbered from the left or from the right looking toward the screen? (L/R) \n").upper()

        while direction != "L" and direction != "R":
            direction = input(
                "\nAre seats to be numbered from the left or from the right looking toward the screen? (L/R) \n").upper()

        def count_from_left():
            for i in range(1, rows+1):
                print(f'Row {i:^3}  |  ', end='')
                for j in range(1, seats+1):
                    print(f"{j} ", end='')
                print('  |')
            print()

        def count_from_right():
            for i in range(1, rows+1):
                print(f'Row {i:^3}  |  ', end='')
                for j in range(seats, 0, -1):
                    print(f"{j} ", end='')
                print('  |')
            print()

        print(f"\n      {' S c r e e n ':*^{seats*3}}\n")

        if direction == "L":
            count_from_left()
        elif direction == "R":
            count_from_right()

    except:
        cinema()


cinema()
