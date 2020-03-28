import pyCrackNg
import os

# pyCrackNg.airmon("wlp2s0")



# print(see_if_available[10:15])
# get_aircrackng = os.popen("echo hc20030222 | sudo -S c").read()
# see_if_available = get_aircrackng.split()
# if see_if_available[10:15] == ['is', 'already', 'the', 'newest', 'version']:
#     print("It is already installed...")
# else:
#     print("installing")

if os.getuid() == 0:
    print("Finding aircrack-ng...")
    find_application = os.popen("dpkg -l | grep aircrack-ng").read()

    if find_application == "":
        print("\nWe couldn't find it : installing it")
        os.system("apt-get -y install aircrack-ng")
    else:
        print("Found the program!")
        # os.popen("apt-get remove --purge -y weather-util weather-util-data")

    testing = os.popen("apt-get install weather-util").read()
    see_if_available = testing.split()
else:
    print("must be root")

# for i in see_if_available:
#     if i == "already":
#         print("This program is in the system")
#     else:
#         print("Installing program")
#         break

# if os.getuid() == 0:
#     # print("it is in root")
#     os.system("apt-get install aircrack-ng")
# else:
#     print("must be in root")