#!/bin/bash
CHANNEL_ID="@modelcollector3d"
sendMessage() {
  curl \
    -s -X POST https://api.telegram.org/bot$TELEGRAM_TOKEN/sendMessage \
    -d chat_id="$1" \
    -d text="$2"
}

# Read the file into a list
while IFS= read -r line; do
  sendMessage $CHANNEL_ID $line
  sleep 5
done < list.txt
