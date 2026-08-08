import logging
import logging.config
import warnings
from pyrogram import Client, idle
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from config import Config
from aiohttp import web
from plugins.web_support import web_server
from pytz import timezone
from datetime import datetime
import asyncio
from plugins.syd_rename import process_queue, db
import pyromod
from pyrogram import utils as pyroutils

pyroutils.MIN_CHAT_ID = -999999999999
pyroutils.MIN_CHANNEL_ID = -100999999999999

logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pymongo").setLevel(logging.ERROR)


class Bot(Client):

    def __init__(self):
        super().__init__(
            name="For",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=15,
        )

        self.log_message = None
        self.log_task = None
        self.log_times = []

    async def log_time_loop(self):
        """Edit one message every 6 minutes with the latest 20 IST timestamps."""

        while True:
            try:
                ist = timezone("Asia/Kolkata")
                now = datetime.now(ist)

                timestamp = now.strftime("%d-%m-%Y %I:%M:%S %p")

                # Add newest timestamp
                self.log_times.append(timestamp)

                # Keep only latest 20
                self.log_times = self.log_times[-20:]

                text = "🟢 **Bot Activity Log**\n\n"

                # Newest first
                for i, time in enumerate(reversed(self.log_times), 1):
                    text += f"`{i}.` {time} IST\n"

                if self.log_message:
                    try:
                        await self.log_message.edit_text(text)
                    except Exception as e:
                        logging.error(f"Failed to edit log message: {e}")

                # Wait 6 minutes
                await asyncio.sleep(360)

            except asyncio.CancelledError:
                break

            except Exception as e:
                logging.error(f"Log loop error: {e}")
                await asyncio.sleep(30)

    async def start(self):
        await super().start()

        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username

        app = web.AppRunner(await web_server())
        await app.setup()

        bind_address = "0.0.0.0"
        await web.TCPSite(
            app,
            bind_address,
            Config.PORT
        ).start()

        logging.info(
            f"{me.first_name} ✅✅ BOT started successfully ✅✅"
        )

        # ==============================
        # LOG CHANNEL MESSAGE
        # ==============================

        try:
            self.log_message = await self.send_message(
                Config.LOG_CHANNEL,
                "🟢 **Bot Activity Log**\n\nStarting..."
            )

            self.log_task = asyncio.create_task(
                self.log_time_loop()
            )

        except Exception as e:
            logging.error(
                f"Unable to start log time loop: {e}"
            )

        # ==============================
        # OTHER BOTS
        # ==============================

        if Config.WOOK:
            syyd = Client(
                "SyDLnK",
                api_hash=Config.API_HASH,
                api_id=Config.API_ID,
                plugins={
                    "root": "SyD"
                },
                workers=50,
                bot_token=Config.SYD_TOKEN
            )

            try:
                await syyd.start()
            except Exception as e:
                logging.info(f"{e}")

        if Config.FOR_TOKEN:
            sydfor = Client(
                "SyDnK",
                api_hash=Config.API_HASH,
                api_id=Config.API_ID,
                plugins={
                    "root": "Mr-SyD"
                },
                workers=50,
                bot_token=Config.FOR_TOKEN
            )

            try:
                await sydfor.start()
            except Exception as e:
                logging.info(f"{e}")

        if Config.FOR2_TOKEN:
            sydfor2 = Client(
                "SyDLnKk",
                api_hash=Config.API_HASH,
                api_id=Config.API_ID,
                plugins={
                    "root": "Mr-SyD"
                },
                workers=50,
                bot_token=Config.FOR2_TOKEN
            )

            try:
                await sydfor2.start()
            except Exception as e:
                logging.info(f"{e}")

        # if await db.count() != 0:
        #     asyncio.create_task(process_queue(self))

        for id in Config.ADMIN:
            try:
                await self.send_message(
                    id,
                    f"**__{me.first_name} Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️__**"
                )
            except:
                pass

    async def stop(self, *args):

        # Stop log loop
        if self.log_task:
            self.log_task.cancel()

            try:
                await self.log_task
            except asyncio.CancelledError:
                pass

            self.log_task = None

        await super().stop()

        logging.info("Bot Stopped 🙄")


bot = Bot()
bot.run()
