import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait


SOURCE_CHAT = [-1003769564318, -1003778649901, -1004489264718, -1004235033201, -1004485913563]
DUMP_CHAT = -1002287749434

sem = asyncio.Semaphore(2)


@Client.on_message(filters.chat(SOURCE_CHAT) & (filters.video | filters.document))
async def live_forward(client, message):
    async with sem:
        while True:
            try:
                await client.copy_message(
                    chat_id=DUMP_CHAT,
                    from_chat_id=SOURCE_CHAT,
                    message_id=message.id
                )

                print(f"Forwarded: {message.id}")
                await asyncio.sleep(5)
                return

            except FloodWait as e:
                wait = e.value + 2
                print(f"FloodWait {e.value}s -> Sleeping {wait}s")
                await asyncio.sleep(wait)

            except Exception as err:
                print(f"Failed {message.id}: {err}")
                return

