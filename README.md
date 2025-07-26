# Port Scanner Module - Internship Project

This project implements a foundational penetration testing tool: a Port Scanner. It identifies open ports on target systems using a basic socket-based scanner and an advanced Nmap-integrated scanner.

Designed as the first internship task, this module focuses on essential reconnaissance. Port scanning is a critical initial step in penetration testing, revealing active services and potential entry points. Understanding open ports and listening services helps identify vulnerabilities and plan attacks, laying the groundwork for subsequent exploitation by mapping the target's network.

# Table of Contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Ethical Considerations](#ethical-considerations)
6. [Project Structure](#project-structure)
7. [Troubleshooting Common Issues](#troubleshooting-common-issues)

# Features

**Socket-based Port Scanner:** A basic scanner using Python's `socket` module. It attempts raw TCP connections to target ports. Successful connections indicate an open port. This scanner helps understand fundamental network communication and TCP/IP handshakes. It efficiently checks user-defined port ranges, providing a quick overview of directly accessible services. Its simplicity is excellent for grasping network basics.

**Nmap-integrated Port Scanner:** This advanced scanner leverages the industry-standard Nmap command-line tool via the `python-nmap` library. Nmap offers sophisticated scanning techniques like SYN scans, UDP scans, and comprehensive version detection. It accurately identifies specific applications and their versions (e.g., Apache HTTP Server 2.4.41, OpenSSH 8.2p1) and performs OS fingerprinting (e.g., Linux 5.x, Windows Server 2019). This integration provides a richer, more accurate picture of the target's attack surface, vital for real-world scenarios where software versions link to known vulnerabilities.

 **Menu-driven Framework:** The entire project is encapsulated within a simple command-line interface (`pentest_framework.py`). This interactive menu allows users to easily select and execute either the basic socket-based scanner or the powerful Nmap-integrated scanner. This modular design enhances usability and provides a clear, extensible entry point for future tool integration, promoting maintainability and scalability.

# Prerequisites

Ensure the following software is installed and configured:

**Python 3.x:** (Recommended 3.8+). Core programming language for all scripts.
    * Download from [python.org](https://www.python.org/downloads/).

**pip:** Python's package installer, essential for third-party libraries. Verify with `pip --version`.

**Virtual Environment (`venv`):** Highly recommended for isolated, project-specific dependencies.

**Nmap:** Command-line port scanning tool.
   **Windows:** Installer from [nmap.org/download.html](https://nmap.org/download.html). **Ensure "Add Nmap to your system PATH" is checked.**
   **Linux/macOS:** Install via package manager (e.g., `sudo apt-get install nmap`, `brew install nmap`).

**Npcap (for Windows):** Packet capture driver required by Nmap.
  **Download from [npcap.com](https://npcap.com/). **Check "Install Npcap in WinPcap API-compatible mode" during installation.**
  **Restart your computer** after installation.

# Installation

1.  **Clone/Download Project Files:** Place `pentest_framework.py`, `port_scanner.py`, `nmap_scanner.py`, and `README.md` into a dedicated folder (e.g., `D:\VS Code\Port Scanner project`).

2.  **Navigate to Project Directory:**
    ```bash
    cd "D:\VS Code\Port Scanner project"
    ```

3.  **Create a Virtual Environment:**
    ```bash
    python -m venv .venv
    ```

4.  **Activate the Virtual Environment:**
     **Windows (PowerShell/CMD):** `.\.venv\Scripts\activate`
     **Linux/macOS (Bash/Zsh):** `source ./.venv/bin/activate`
    * Prompt will show `(.venv)`.

5.  **Install Python Dependencies:**
    * With `(.venv)` active, install `python-nmap`:
        ```bash
        pip install python-nmap
        ```

# Usage

1.  **Open VS Code as Administrator (Recommended for Nmap on Windows):** Right-click VS Code icon, select "Run as administrator."

2.  **Open Project Folder in VS Code:** `File > Open Folder...`, select `D:\VS Code\Port Scanner project`.

3.  **Open Integrated Terminal:** `Terminal > New Terminal` (`Ctrl + `).

4.  **Activate Virtual Environment:** (Refer to [Installation](#installation) step 4 if needed).

5.  **Run the Framework:**
    ```bash
    python pentest_framework.py
    ```

6.  **Select a Scanner Option:** Choose `1` (Socket-based) or `2` (Nmap-integrated). Follow prompts for target IP/hostname (e.g., `192.168.1.1`, `scanme.nmap.org`) and port range (e.g., `1-1000`, `22,80,443`).

**Example Targets for Ethical Testing (Crucial!):**

**Localhost:** `127.0.0.1` or `localhost` (safe, self-scan).

 **Virtual Machines:** Intentionally vulnerable VMs you control, like [Metasploitable2](https://docs.rapid7.com/metasploit/metasploitable-2/) or a [Kali Linux VM](https://www.kali.org/get-kali/).
    * Obtain VM IP from its console (`ip addr show`).
    * For SSH on older VMs, `ssh -oHostKeyAlgorithms=+ssh-rsa <user>@<ip>` may be needed for manual connections.

# Ethical Considerations

**WARNING:** Penetration testing tools are powerful. Misuse can cause harm and lead to severe legal consequences.

 **ALWAYS obtain explicit, written permission** from the system owner before scanning. Define scope, duration, and type of testing.

 **NEVER use these tools on unauthorized systems.** Unauthorized scanning is illegal and unethical.

 **Use these tools ONLY in controlled, isolated lab environments** you own and manage (e.g., your VMs).

 **Understand the impact:** Even passive scanning can trigger IDS/IPS or cause minor disruptions. Prioritize learning and ethical conduct.

# Project Structure
Port Scanner project/
├── .venv/                   # Python virtual environment
├── pentest_framework.py     # Main menu and framework launcher
├── port_scanner.py          # Socket-based scanner
├── nmap_scanner.py          # Nmap-integrated scanner
└── README.md                # Project documentation

# Troubleshooting Common Issues

 **`ModuleNotFoundError` (for `nmap`, `port_scanner`, `nmap_scanner`):**
    * Ensure `(.venv)` is active in terminal.
    * Install `python-nmap` in active `venv` (`pip install python-nmap`).
    * Verify VS Code's Python interpreter points to `.venv` (bottom-left corner).
    * `Ctrl+Shift+P`, `Python: Clear Workspace Cache and Reload Window`.
    * Confirm `port_scanner.py` and `nmap_scanner.py` are directly in the project folder and named exactly.

 **`Nmap scan error: nmap program was not found in path.`:**
    * Nmap (command-line tool) is not installed or not in system PATH. See [Prerequisites](#prerequisites).

 **"No hosts found or scanned" from Nmap (or scan finishes too quickly):**
    * Nmap installed and in PATH.
    * **Run VS Code as Administrator** (see [Usage](#usage) step 1). Critical for Nmap on Windows.
    * Npcap installed and computer restarted (see [Prerequisites](#prerequisites)).
    * Target IP correct, online, and reachable (`ping <target_ip>` from Admin CMD).
    * Check host/target firewalls.

 **`Connection timed out` or `Connection refused` (socket scanner/manual SSH):**
    * Target VM/host is on, operational, and network adapter configured.
    * Specific service (e.g., SSH on port 22) is running on target.
    * Check firewalls (host/target). For older VMs, manually enable/start SSH service (`sudo systemctl start ssh`) and check `iptables` (`sudo iptables -L -n`).
    * For manual SSH/SCP to older VMs, use `-oHostKeyAlgorithms=+ssh-rsa`.

    **This project is awesome!**
