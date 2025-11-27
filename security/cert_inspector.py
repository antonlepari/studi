#!/usr/bin/env python3
import subprocess, sys

if len(sys.argv) != 2:
    print("Usage: python3 cert_inspector.py <domain>")
    exit(1)

domain = sys.argv[1]

cmd = [
    "openssl", "s_client",
    "-connect", f"{domain}:443",
    "-servername", domain
]

try:
    print(f"🔍 Fetching certificate for {domain}...\n")
    out = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=10)
    print(out.decode())
except Exception as e:
    print("Error:", e)
