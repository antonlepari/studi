#!/bin/bash

echo "🔐 Active iptables rules:"
echo "-------------------------"
sudo iptables -L -n -v

echo ""
echo "🔥 Checking if SSH (22) and HTTPS (443) are allowed..."
echo ""

for port in 22 443; do
    sudo iptables -L INPUT -n | grep "dpt:$port" > /dev/null
    if [ $? -eq 0 ]; then
        echo "✔ Port $port is ALLOWED"
    else
        echo "❌ Port $port is BLOCKED"
    fi
done
