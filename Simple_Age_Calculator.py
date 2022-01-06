from datetime import date

print("*"*50+" Hello I'm A Simple Age Calculator "+"*"*50)
print()
print("*"*50+" I Will Help U Now To Know Your Age "+"*"*50)

birth = int(input("\nIn which year were you born?\n"))

now = int(date.today().year)


the_age = now - birth

while True:

    answer = input("Do you want to know your age? (YES / NO) \n")

    if answer.lower() == "yes":
        print(f"\nYour age is: {the_age}")
        print("*" * 50 + " THANKS FOR USING ME " + "*" * 50)
        break

    elif answer.lower() == "no":
        print("*"*50+" THANKS FOR USING ME "+"*"*50)
        break

    else:
        print("\n" * 2 + "-" * 50 + "Wrong Input! Please Type 'Yes' or 'No'" + "-" * 50 + "\n" * 2)
