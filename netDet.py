import os # For all the terminal based commands
import subprocess
import shlex

os.popen("chmod +x repeat-search.sh")
os.popen("rm -f airdump_info/result*")

# This will check the terminal if it's in root
if os.geteuid() == 0:

    # ----------------------------------------------------------------------
    # Checking if aircrack is available
    print("\033[32mChecking if 'aircrack-ng' is installed...\033[39m")
    find_aircrack = os.popen("dpkg -l | grep aircrack-ng").read()
    if find_aircrack == "":
        print("\033[31mUnable to find the program\033[39m : installing it\n")
        os.popen("apt-get -y install aircrack-ng")
    else:
        print("Aircrack-ng was found in your computer!\n")

    # ----------------------------------------------------------------------

    print("Enter internet connection type (i, g; wlp2s0)")
    internet = input(" > ")
    print("Enter devices BSSID (i, g; B8:A3:86:4B:31:E2)")
    bssid = input (" > ")

    def start_detection():
        os.popen(f"airmon-ng start {internet}")

        print("Getting information using 'airodump-ng'...")

        while True:
            usr_input = input("\nThe program make your device go offline until you exit out the program. Will you still like to continue? [y / n] > ")

            if usr_input.lower() == "y":

                print("Disconnecting device & starting the loop...")
                
                print("Good night!")

                subprocess.call(shlex.split(f"gnome-terminal -- bash repeat-search.sh {internet} {bssid}"))
                break

            elif usr_input.lower() == "n":
                print("\nProceeding to exit the program...")
                exit()
            else:
                print("\nInvalid input")
    
    start_detection()

    # ----------------------------------------------------------------------

    # The main terminal emulation

    while True:
        usr_input = input("netDet> ").lower()

        if usr_input == "trusted":
            f = open("airdump_info/_TRUSTED_DEVICES.txt", "r")
            for i in f:
                print(i)

        elif usr_input == "detection":
            f = open("airdump_info/_UNTRUSTED_DEVICES.txt", "r")
            for i in f:
                print(i)
        
        elif usr_input == "start":
            while True:
                x = input("Are you sure? [ y / n ] > ").lower()

                if x == "y":
                    start_detection()
                else:
                    print("Alright")
                    break

        elif usr_input == "q" or usr_input == "exit":
            
            os.popen(f"airmon-ng stop {internet}mon")
            print("Finished going back to the network")
            print("\nREAD: Keep in mind, you might need to reboot the system to go back to the internet...If your device didn't go back to the wifi, simply enter in your terminal 'airmon-ng stop (internet type)mon'.\n")
            print("Thank you, come again!")
            break

        elif usr_input == "help":
            print("""
trusted     It will list all the trusted devices from text file
            you have entered.

detection   Will compare the list you've given over 'aircrack-ng'
            and will return the results wether or not it detected
            an untrusted device. (Still in progress...)

start       Will begin the program again, sleep tight :)

q / exit    Exit out the program.
            """)

        else:
            print("Command undifined, enter help for commands")

        # ----------------------------------------------------------------------

else:
    print("You must be in root to run this script...")