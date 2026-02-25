import re
from collections import defaultdict
from datetime import datetime

log_file = "sample.log"

failed_attempts = defaultdict(int)
successful_logins = []
alerts = []

# Business hours (8 AM - 6 PM)
BUSINESS_START = 8
BUSINESS_END = 18

with open(log_file, "r") as file:
    for line in file:
        
        # Detect failed login attempts
        if "Failed password" in line:
            ip_match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
            if ip_match:
                ip = ip_match.group(1)
                failed_attempts[ip] += 1

        # Detect successful logins
        if "Accepted password" in line:
            ip_match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
            time_match = re.search(r'(\w+\s+\d+\s+\d+:\d+:\d+)', line)

if ip_match and time_match:
    ip = ip_match.group(1)
    time_str = time_match.group(1)

    # Add current year to avoid deprecation warning
    current_year = datetime.now().year
    login_time = datetime.strptime(f"{current_year} {time_str}", "%Y %b %d %H:%M:%S")
    hour = login_time.hour

    if hour < BUSINESS_START or hour > BUSINESS_END:
        alerts.append(f"⚠ Suspicious login time from {ip} at {hour}:00")

# Detect brute-force attempts
for ip, count in failed_attempts.items():
    if count >= 3:
        alerts.append(f"🚨 Possible brute-force attack from {ip} ({count} failed attempts)")

# Generate report
with open("report.txt", "w", encoding="utf-8") as report:
    report.write("=== SECURITY REPORT ===\n\n")
    for alert in alerts:
        report.write(alert + "\n")

print("Analysis complete. Check report.txt")