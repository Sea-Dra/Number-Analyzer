name = input("Enter your name: ")

running = True

while running:
    num = int(input("Enter an integer # between 1 and 100: "))
    if 0 < num <= 100:

        if num % 2 == 1 and num < 60:
            print(f"{name} entered the number {num}. Odd and less than 60")
        elif num % 2 == 0 and 2 < num < 25:
            print(f"{name} entered the number {num}.Even and less than 25")
        elif num % 2 == 0 and 26 <= num <= 60:
            print(f"{name} entered the number {num}. Even and between 26 and 60 inclusive")
        elif num % 2 == 0 and num > 60:
            print(f"{name} entered the number {num}. Even and greater than 60")
        elif num % 2 == 1 and num > 60:
            print(f"{name} entered the number {num}. Odd and greater than 60")
    else:
        print(f"The number entered by {name} is not between 1 and 100")
    Answer = input("Would you like to run it again? yes/no")
    if Answer == "yes":
        continue
    else:
        running = False
