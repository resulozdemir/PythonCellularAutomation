# Week 6 Report

## Tasks and Progress Status

### 1. PPP Protocol Installation
- The installation of the modem PPP protocol is made ready with AT commands (AT+QCFG="usbnet",0)
- Sixfab_PPP_Installer github repo was cloned and questions such as modem type were answered.
- The installation was successful and the modem was restarted.
- After the modem was restarted, 'sudo pon' command was run but 'Modem hangup Connection terminated.' error received.
- To solve the error, solutions in articles with similar errors on community.sixfab.com were tried, but the problem could not be solved.

![Alt text](ppp_error.jpg)
### 2. QMI/RMNET Protocol Installation

- The installation of the modem QMI protocol is made ready with AT commands (AT+QCFG="usbnet",0)
- libqmi installation has been completed.
- When the 'sudo qmicli -d /dev/cdc-wdm0 --dms-get-operating-mode' command is run in the terminal, 'error: couldn't create QmiDevice: Couldn't query file info: Error when getting information for file “/dev/ cdc-wdm0”: 'No such file or directory' error was received.

### 3. ECM Protocol Installation and Speed Testing
- Internet connection was established with ECM protocol and the speed test was performed successfully.

![Alt text](<ECM Speed Test.jpg>)

## References
- [Setting up the PPP connection](https://docs.sixfab.com/page/setting-up-the-ppp-connection-for-sixfab-shield-hat)
- [Setting up a data connection over QMI interface using libqmi](https://docs.sixfab.com/page/setting-up-a-data-connection-over-qmi-interface-using-libqmi)
- [Internet Connection with Twilio Super SIM, EC25 and Sixfab Base HAT using ECM](https://docs.sixfab.com/page/internet-connection-by-using-sixfab-base-hat-and-twilio-super-sim-via-ecm)