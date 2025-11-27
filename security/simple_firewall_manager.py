#!/usr/bin/env python3
import subprocess, sys

def run(cmd):
    print(">", " ".join(cmd))
    subprocess.call(cmd)

def allow(port):
    run(["sudo", "iptables", "-A", "INPUT", "-p", "tcp", "--dport", port, "-j", "ACCEPT"])

def block(port):
    run(["sudo", "iptables", "-A", "INPUT", "-p", "tcp", "--dport", port, "-j", "DROP"])

if len(sys.argv) < 3:
    print("Usage: python3 simple_firewall_manager.py <allow|block> <port>")
    exit(1)

action = sys.argv[1]
port = sys.argv[2]

if action == "allow":
    allow(port)
elif action == "block":
    block(port)
else:
    print("Unknown command")
