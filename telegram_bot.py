import requests
import os

# Go to telegram and look for BotFather,
# meet with him and ask to have your own bot
# copy the token that he gives you
# use token in: https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
# send a message to the bot in telegram
# reload page to get the chat id

BOT_TOKEN=os.getenv("BOT_TOKEN")
CHAT_ID=os.getenv("CHAT_ID")
CHAT_ID_LIST=CHAT_ID.split(";")
#print (CHAT_ID_LIST)
with open("output/output.txt", "r") as f:
    MESSAGE=f.read()
for i in CHAT_ID_LIST:
    url=f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload={"chat_id":i, "text":MESSAGE}
    response=requests.post(url,data=payload)

    if response.status_code==200:
        print("Message sent successfully!")
    else:
        print("Failed to send message:", response.text)