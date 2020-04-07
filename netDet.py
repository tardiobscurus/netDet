import os # For all the terminal based commands
import csv # To read the given devices connected to the network

detected_untrusted_device = False

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

    print("Getting information using 'airodump-ng'...")

    while True:
        usr_input = input("\nThe program make your device go offline until you exit out the program. Will you still like to continue? [y / n] > ")

        if usr_input.lower() == "y":

            # Plans for this section
            # - We will open up a new terminal for sequencing airdump
            # - Within this part, we will try and retrive info only in the devices STATION's bssid (if possible)
            # - That info will be sent to a text file, when running again, if found that text file, it will overwrite it

            print("Disconnecting device & listing connected devices in network...")
            print("It will take ~45 seconds...")
            os.system(f"sh grab_devices.sh {internet}")

            print("Finished finding information using 'airodump-ng'\n")
            break
        elif usr_input.lower() == "n":
            print("\nProceeding to exit the program...")
            exit()
        else:
            print("\nInvalid input")

    # ----------------------------------------------------------------------

    while True:
        file_inp = str(input("Enter in the file name of trusted devices > "))
        result = os.popen("find -name " + file_inp).read()
        if result == "":
            print("Couldn't find that...")
        else:
            print("Found the text file!\n")
            break

    # ----------------------------------------------------------------------

    print("Running through dignostics...")
    if not detected_untrusted_device:
        print("\033[32mNo detected untrusted devices found.\033[39m\n")
    else:
        print("\033[31mDetected an untrusted device in the WiFi, enter 'detection' to see more detail.\033[39m\n")
        # break

    # ----------------------------------------------------------------------

    # The main terminal emulation

    while True:
        usr_input = input("netDet> ") trusted

        if usr_input == "trusted":
            f = open(file_inp, "r")
            for i in f:
                print(i)

        elif usr_input == "detection":
            print("In progress...")

        elif usr_input == "q" or usr_input == "exit":
            # os.system(f"gnome-terminal --window -- sh -c \"echo {psswrd_input} | sudo -S \"service network-manager start\"")
            # os.system("service network-manager start && exit")

            # In this we will
            # - Stop the monitor mode in airmon-ng
            # - Restart network-manager
            # - Disclaim the viewer that you may need to reboot the system to go back to the network.
            # - Lastly, of course, exit out the program
            
            os.popen(f"airmon-ng stop {internet}mon")
            print("Finished going back to the network")


            print("Thank you, come again!")
            break

        elif usr_input == "help":
            print("""
trusted     It will list all the trusted devices from text file
            you have entered.

detection   Will compare the list you've given over 'aircrack-ng'
            and will return the results wether or not it detected
            an untrusted device. (Still in progress...)

q / exit    Exit out the program.
            """)

        else:
            print("Command undifined, enter help for commands")

        # ----------------------------------------------------------------------

else:
    print("You must be in root to run this script...")