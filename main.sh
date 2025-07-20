m#!/bin/bash
TELEGRAM_API_URL="https://api.telegram.org/bot$TELEGRAM_TOKEN/sendMessage"
CHANNEL_ID="@modelcollector3d"
MESSAGE="test message 2"
echo $BOT_TOKEN
sendMessage() {
  curl \
    -s -X POST https://api.telegram.org/bot$TELEGRAM_TOKEN/sendMessage \
    -d chat_id="$1" \
    -d text="$2"
}

#sendMessage $CHANNEL_ID $MESSAGE
# curl -s -X POST "https://api.telegram.org/bot${BOT_TOKEN}/sendMessage" \
#     -d chat_id="${CHAT_ID}" \
#     -d text="${MESSAGE}"


  curl \
    -s -X POST https://api.telegram.org/bot$TELEGRAM_TOKEN/sendMessage \
    -d chat_id="$CHANNEL_ID" \
    -d text="$MESSAGE"

    https://api.telegram.org/bot$TOKEN/sendMessage
