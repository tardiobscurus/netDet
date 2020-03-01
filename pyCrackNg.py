from getpass import getpass
import os

def airmon(wireless_network, bssid=""):
    passwrd_input = getpass("[sudo] Password: ", stream=None)
    os.system(f"gnome-terminal --window -- sh -c \"echo {passwrd_input} | sudo -S \"airmon-ng check kill\"; bash\"")
    os.system(f"gnome-terminal --window -- sh -c \"echo {passwrd_input} | sudo -S \"airdump-ng start {wireless_network}\"; bash\"")
    
# && exit