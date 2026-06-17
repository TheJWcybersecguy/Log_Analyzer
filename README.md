# Log Analyzer

## Overview
The Log Analyzer is a Python tool designed to help security analysts detect suspicious activities in server authentication logs. It parses log files, identifies patterns such as brute-force attacks and logins outside business hours, and generates a clear security report.

This project simulates a real SOC workflow and demonstrates log monitoring, basic cybersecurity analysis, and automation.

## Features
- Detects multiple failed login attempts (possible brute-force attacks)
- Flags logins outside business hours (suspicious access)
- Generates a report.txt file with all alerts
- Handles Unicode characters (e.g., ⚠, 🚨) safely
- Future-proof date handling by adding the **current year** for log entries

## Requirements
- Python 3.x installed
- Works on Windows, Linux, or macOS
- No external libraries required

## Setup & Usage
1. Clone or download the project folder.
2. Ensure `sample.log` is in the same folder as `analyzer.py`.
3. Open a terminal in the project folder.
4. Run the script:

```bash
py analyzer.py

# Log_Analyzer
Python tool for analyzing server authentication logs for SOC
