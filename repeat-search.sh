INTERNET=$1
BSSID=$2

airmon-ng start $INTERNET > /dev/null 2>&1
> airdump_info/_UNTRUSTED_DEVICES.txt
rm -f airdump_info/result*

while :
do
    printf "[ $(date +%T) ] Getting devices...\n"
    gnome-terminal -- timeout 55 airodump-ng --bssid ${BSSID} -c 2 -w airdump_info/result ${INTERNET}mon > /dev/null 2>&1
    sleep 55s
    awk 'NR >= 6' airdump_info/result-01.csv | cut -d ',' -f 1-1 >> airdump_info/_DETECTED_DEVICES.txt
    sed -i '/^[[:space:]]*$/d' airdump_info/_DETECTED_DEVICES.txt

    if [ -z $(grep -Fvxf airdump_info/_TRUSTED_DEVICES.txt airdump_info/_DETECTED_DEVICES.txt) ]; then
        rm -f airdump_info/result*
        printf "No detected devices...\n"
        > airdump_info/_DETECTED_DEVICES.txt
    else
        grep -Fvxf airdump_info/_TRUSTED_DEVICES.txt airdump_info/_DETECTED_DEVICES.txt >> airdump_info/_UNTRUSTED_DEVICES.txt
        printf "Found untrusted device(s)!\n"
        echo   "------------------------"
        grep -Fvxf airdump_info/_TRUSTED_DEVICES.txt airdump_info/_DETECTED_DEVICES.txt
        echo   "------------------------"
        echo "Deauthanticating device until user responds..."
        aireplay-ng --deauth 0 -c "$(grep -Fvxf airdump_info/_TRUSTED_DEVICES.txt airdump_info/_DETECTED_DEVICES.txt)" -a $BSSID ${INTERNET}mon > /dev/null 2>&1
        rm -f airdump_info/result*
        > airdump_info/_DETECTED_DEVICES.txt
        break
    fi
done
