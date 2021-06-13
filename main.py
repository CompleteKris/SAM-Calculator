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

    num_of_s_sub = input("Instert number of school subject (14) :\n\n")
    num_of_s_sub = int(num_of_s_sub)

    s_subjects = []

    for i in range(int(num_of_s_sub)):
        s_sub = input("Instert final grade of " + str(i+1) + " subject:\n\n")
        s_subjects.append(int(s_sub))

    s_subjects = sum(s_subjects)
    s_subjects = s_subjects/num_of_s_sub

    print("Arithmetic mean is: " + str(s_subjects))

    # ending script
    con = input("Press enter to exit or something else + enter to start again!")

    if con == "":
        exit()
    else:
        pass