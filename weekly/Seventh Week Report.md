# Week 7 Report

## Tasks and Progress Status

### 1. PPP Installation
- The modem software was written to use ECM, So, the error "Modem hangup Connection terminated." happened. It was fixed with these commands:

    ```Bash
	sudo systemctl stop core_manager core_agent
	sudo systemctl disable core_manager core_agent

- A speed test was done.

![PPP Speed Test](<PPP speed test.png>)

### 2. QMI Installation
- QMI installation was successfully completed.
- A speed test was done.

![QMI Speed Test](<QMI speed test.png>)

### 3. Writing Final Report of Project
- The final report for the project was writed.

---

## Protocol Comparison: PPP, QMI, ECM

### PPP (Point-to-Point Protocol)
- **Usage:** Typically used for internet connection over telephone lines.
- **Features:** Supports IP, offers authentication and error control.

### QMI (Qualcomm MSM Interface)
- **Usage:** For 3G and 4G LTE connections, in mobile devices and data cards.
- **Features:** Fast data transmission, low latency, controls modem functions.

### ECM (Ethernet Control Model)
- **Usage:** For communication over Ethernet among USB devices.
- **Features:** Network connection via USB, used in IoT devices and mobile devices.

### Comparison
- **PPP:** Broad application range, compatible with older technologies.
- **QMI:** Optimized for mobile connections, focused on speed and low latency.
- **ECM:** For network connectivity in USB-connected devices, specific use cases.

---

## References
- [Sixfab PPP Guide](https://docs.sixfab.com/page/setting-up-the-ppp-connection-for-sixfab-shield-hat)
- [Sixfab QMI Huide](https://docs.sixfab.com/page/setting-up-a-data-connection-over-qmi-interface-using-libqmi)