import os
import pyCrackNg
from getpass import getpass
# import subprocess

# subprocess.run(["ls", "-l"])

psswrd_input = getpass(prompt="[sudo] Password: ", stream=None)

no_detected_untrusted_device = False

if psswrd_input == "hc20030222":
    print("Getting information using airodump-ng...")
    
    while True:
        inp_continue = input("If you continue, you will be temporarily disconnected from the network until you exit the program by entering \"q\". Are you sure to continue? [Y / N] > ")
        if inp_continue.upper() == "Y":
            os.system(f"gnome-terminal --window -- sh -c \"echo {psswrd_input} | sudo -S \"airmon-ng\" && exit; bash\"")
            print("Finished finding information using airodump-ng")

            while True:
                file_inp = str(input("Enter in the file name of trusted devices > "))
                result = os.popen("find -name " + file_inp).read()
                if result == "":
                    print("Couldn't find that...")
                else:
                    print("Found it!")
                    break
            
            print("Received information!")

            print("Running through dignostics...")
            if not no_detected_untrusted_device:
                print("\033[31mDetected an untrusted device in the WiFi, enter 'detection' to see more detail.\033[39m")
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

        elif usr_input == "detection":
            print("In progress...")

        elif usr_input == "q":
            # os.system(f"gnome-terminal --window -- sh -c \"echo {psswrd_input} | sudo -S \"service network-manager start\"")
            os.system(f"echo {psswrd_input} | sudo -S \"service network-manager start\"")
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