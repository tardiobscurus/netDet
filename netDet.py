import os
# import subprocess

# subprocess.run(["ls", "-l"])

psswrd = "hc20030222"
psswrd_input = input("Password: ")

no_detected_untrusted_device = True

if psswrd_input == psswrd:
    print("Getting information using airodump-ng...")

    while True:
        inp_continue = input("If you continue, you will be temporarily disconnected from the network until you exit the program by entering \"q\". Are you sure to continue? [Y / N] > ")
        if inp_continue.upper() == "Y":
            os.system("gnome-terminal --window -- sh -c \"echo " + psswrd + " | sudo -S \"airmon-ng\" && exit; bash\"")

            file_inp = str(input("Enter in trsuted devices file location > "))
            os.system("find " + file_inp)
            
            print("Received information!")

            print("Running through dignostics...")
            if not no_detected_untrusted_device:
                print("\033[31mDetected an untrusted device in the WiFi, enter --- to see more detail.\033[39m")
            else:
                print("\033[32mNo detected untrusted devices found.\033[39m")
            break
        elif inp_continue.upper() == "N":
            print("Exiting out of the program...")
            exit()
        else:
            print("Invalid input, try again...")

    while True:
        usr_input = input("netDet> ")

        if usr_input == "trusted":
            f = open(file_inp, "r")
            for i in f:
                print(i)

        elif usr_input == "q":
            print("Thank you, come again!")
            break

        elif usr_input == "--help":
            print("""
trusted     It will list all the trusted devices from text file
            you have entered.

q           You will be automatically be exitted out of the 
            program, and you will be coming back to the program.
            """)

        else:
            print("Command undifined, enter --help for commands")
else:
    print("No, you are not allowed, go away!")