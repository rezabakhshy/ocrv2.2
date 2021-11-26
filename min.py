from typing import Text
from pyrogram import Client,filters
import os
app = Client("my_accound",api_id=12721742,api_hash="2a81674bd5e1ccbaed8c07f898d614ca")

@app.on_message(filters.text)
def ocr(client, message):
    text=message.text
    text2=text.split()[0]
    if text2=="!ocr":
        text=message.reply_to_message.photo.file_id
        client.download_media(text,"test.jpg")
        client.send_photo("ocr_prov_bot","downloads/test.jpg")
        os.remove("downloads/test.jpg")
       
    elif message.reply_to_message:
            client.send_message("rezabz2",text)

app.run()
