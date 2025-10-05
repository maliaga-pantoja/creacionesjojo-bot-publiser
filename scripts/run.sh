#!/bin/bash


sendMessage() {
  curl \
    -s -X POST https://api.telegram.org/bot$TELEGRAM_TOKEN/sendMessage \
    -d chat_id="$1" \
    -d text="$2"
}

# # Read the file into a list
# while IFS= read -r line; do
#   sendMessage $CHANNEL_ID $line
#   sleep 5
# done < list.txt
FILE_LINES=$(grep -c '' $AD_FILE)
echo "total lines: $FILE_LINES"
R=$(shuf -i1-$FILE_LINES -n1)
echo "random line: $R"
CONTENT=$(head -n $R $AD_FILE | tail -1)
sendMessage $CHANNEL_ID $CONTENT