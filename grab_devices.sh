# echo "This is you network connection: $1"

# Will open up a new terminal executing the command to 
# gnome-terminal -- sudo apt-get upgrade > /dev/null 2>&1

# gnome-terminal -- \
# airmon-ng start $1 && \
# timeout 45 airodump-ng -w airodump_info/first_detection/simpleDetect/. $1mon &&\
# tail --line 2 airodump_info/first_detection/simpleDetect.-01.csv | cut -d ',' -f 1-1 >> BSSID.txt && echo "Completed network find..."\
# tail -n +6 airodump_info/first_detection/simpleDetect.-01.csv | cut -d ',' -f 1-1 >> text.txt 

# 1. airmon-ng start $1
# 2. timeout 10 airodump-ng -w airdump_info/first_detection/simpleDetect/. $1mon
# 3. tail --line 2 airodump_info/first_detection/simpleDetect/.-01.csv | cut -d ',' -f 1-1 >> BSSID.txt
# 4. timeout 45 airodump-ng --bssid $BSSID -c $CHANNEL -w . $1mon
# 5. 

