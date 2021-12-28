def Age_Calculator():

    birth=float(input("Which Year Did U Born?!! (ONLY YEARS)\n"))
    now= float(input("What Is Date Of Today ?!! (ONLY YEARS)\n"))
    the_age=now-birth
    answer=str(input("Do U Want To Know Your Age?!! (JUST YES OR NO) \n"))

    #the code problem In line 23
    if answer==["yes", "YES", "yES", "Yes"]:
        print(the_age)

    elif answer==["no", "NO", "No", "nO"]:
        print("THANKS")

else:
    print("'ERROR SIR'...........SORRY I CANNOT HELP U........")

Age_Calculator()
