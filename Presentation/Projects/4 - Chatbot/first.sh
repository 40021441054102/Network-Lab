#!/bin/bash

# - Remote IP
REMOTE_IP="192.168.0.101"
# - Remote Port (Local Port of Another Device)
REMOTE_PORT=7337
# - Local Port (Remote Port of Another Device)
LOCAL_PORT=3773

# - Start Listener
socat TCP-LISTEN:$LOCAL_PORT,fork,reuseaddr - &
echo "Started Listener on Port $LOCAL_PORT"

# - Send Messages
while true; do
    read -p "$(whoami): " msg
    echo "$(whoami): $msg" | socat - TCP:$REMOTE_IP:$REMOTE_PORT
done
