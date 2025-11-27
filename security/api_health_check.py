#!/usr/bin/env python3
import subprocess, json, sys

if len(sys.argv) != 2:
    print("Usage: python3 api_health_check.py <url>")
    exit(1)

url = sys.argv[1]

cmd = ["curl", "-s", "-w", "%{http_code}", "-o", "/tmp/api_body.txt", url]

code = subprocess.check_output(cmd).decode().strip()

with open("/tmp/api_body.txt") as f:
    body = f.read()

print(f"URL: {url}")
print(f"Status: {code}")
print("Body:")
print(body)
