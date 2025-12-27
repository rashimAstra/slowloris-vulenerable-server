# Slowloris Lab

⚠️ **Intentionally Vulnerable Project**  
For security learning and testing only. 

---

## Overview

This project simulates an **HTTP server vulnerable to Slowloris (DoS) attacks** by allowing slow, incomplete HTTP headers.

Useful for:
- Learning Slowloris behavior
- Testing security tools
- DoS detection research

---

## Requirements

- Python 3.8+
- No external dependencies

---

## Start the Server

```bash
git clone https://github.com/rashimAstra/slowloris-vulenerable-server.git
cd slowloris-lab
python3 vuln_server.py
