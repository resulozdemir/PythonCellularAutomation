# Week 7 Report

## Tasks and Progress Status

### 1. PPP Installation
- The modem software was written to use ECM, hence the erro "Modem hangup Connection terminated." was encountered. It was resolved by using the commands:

    ```Bash
	sudo systemctl stop core_manager core_agent
	sudo systemctl disable core_manager core_agent

- A speed test was conducted.

![PPP Speed Test](<PPP speed test.png>)

### 2. QMI Installation
- QMI installation was successfully completed.
- A speed test was conducted.

![QMI Speed Test](<QMI speed test.png>)

### 3. Writing Final Report of Project
- The final report for the project was writed.

## References
- [Sixfab PPP Guide](https://docs.sixfab.com/page/setting-up-the-ppp-connection-for-sixfab-shield-hat)
- [Sixfab QMI Huide](https://docs.sixfab.com/page/setting-up-a-data-connection-over-qmi-interface-using-libqmi)