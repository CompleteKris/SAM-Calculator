# SAM-Calculator v1.0
# School arithmetic mean calculator
# By Kris ;)

from sys import exit

# loop
while True:

    # Prints welcome message
    print("""
    
    
    
    
              SCHOOL ARITHMETIC MEAN CALCULATOR v1.0
                           By Kris \n\n\n
    """)

    while True:
        while True:
            num_of_s_sub = input("Instert number of school subjects:\n\n")  # 14
            if num_of_s_sub == "":
                print("You need to insert number, not just enter!\n\n")
            else:
                break
        try:
            num_of_s_sub = int(num_of_s_sub)
            break
        except:
            print("You need to enter number!\n")

    s_subjects = []

    for i in range(int(num_of_s_sub)):
        while True:
            while True:
                s_sub = input("\n\nInstert final grade of " + str(i+1) + " subject:\n\n")
                if s_sub == "":
                    print("You need to type your grade!\n")
                else:
                    break

            try:
                s_subjects.append(int(s_sub))
                break
            except:
                print("You need to enter number!\n")

    s_subjects = sum(s_subjects)
    s_subjects = s_subjects/num_of_s_sub

    print("\n\nArithmetic mean is: " + str(s_subjects))

    # ending script
    con = input("Press enter to exit or something else + enter to start again!")

    if con == "":
        exit()
    else:
        pass