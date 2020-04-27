# **netDet**: Free from hackers over night

**Version 0.2** | **For [Supercomputing Challenge](https://supercomputingchallenge.org/19-20/about.php)**

---

## **About**
With hackers roaming around the world, the most vulnerable within our network is at night when everybody is asleep. This program changes that. With a simple three input command, you will be sleeping soundly knowing that you are protected.

### **How it works**
By using the WiFi security auditing tools suite, [Aircrack-ng](https://github.com/aircrack-ng/aircrack-ng). We will use three of its tools; `airmon-ng`, `airodump-ng`, and `aireplay-ng`. By doing a simple python and BASH script, we can identify, and deauthenticate an untrusted device, found within the WiFi.

### **Downsides and future fixes**

However, the program cannot disconnect more than one device at a time, which will be added in a future version; the program also, cannot detect any device that is connected in a VPN. It is possible, which will come in a future release.

This program is also not yet suitable for the people not knowing what is a BSSID or channel number they are in.

---

## **Install**
**Disclaimer**: It is only available with Debian based Linux Distros. In the future, will be adding more Distros.

Within your terminal, you will clone the repository in a specific directory.

```sh
git clone https://github.com/tardiobscurus/netDet.git
cd netDet/
```

When finally installed, run the Python program found in the repo, keep in mind it must be in root:

```sh
sudo su
(root) python3 netDet.py
```

Follow the given instruction when running the program, and let it run over night. The computer will automatically disconnect the untrusted device based on the text file you've given to the program.
