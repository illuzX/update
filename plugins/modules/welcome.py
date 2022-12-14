import asyncio
from pyrogram import Client as illuzX, filters as Worker, emoji

MENTION = "{}"  
#CHAT = "{}"
MESSAGE = "{}Hey 👮🏼 {}! Welcome to this group"

@illuzX.on_message(Worker.new_chat_members)
async def welcome(client, message):

    new_members = [MENTION.format(message.from_user.mention)for i in message.new_chat_members]

    text = MESSAGE.format(emoji.SPARKLES, ", ".join(new_members))

    dell=await message.reply_text(text, disable_web_page_preview=True)
    await asyncio.sleep(1000)
    await dell.delete()
