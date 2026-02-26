import re
import os
import time

id_pattern = re.compile(r'^.\d+$')


class Config(object):
    # pyro client config
    API_ID = os.environ.get("API_ID", "")  # ⚠️ Required
    API_HASH = os.environ.get("API_HASH", "")  # ⚠️ Required
    SYD_TOKEN = os.environ.get("SYD_TOKEN", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") # ⚠️ Required
    FOR_TOKEN = os.environ.get("FOR_TOKEN", None) # ⚠️ Required
    FOR2_TOKEN = os.environ.get("FOR2_TOKEN", None) # ⚠️ Required
    
    
    DB_URL = os.environ.get("DB_URL", "")
    DB_NAME = os.environ.get("DB_NAME", "")
    # other configs
    BOT_UPTIME = time.time()
    PICS = os.environ.get("PICS", 'https://files.catbox.moe/iq4kp9.jpg https://files.catbox.moe/i6myg1.jpg https://files.catbox.moe/5f0ptk.jpg https://files.catbox.moe/6qvc08.jpg https://files.catbox.moe/iz1r0m.jpg https://files.catbox.moe/cg3wqk.jpg https://files.catbox.moe/ts053n.jpg https://graph.org/file/8c8372dfa0e0ddf8da91d.jpg https://graph.org/file/3b2b8110f6f57f7fc5c74.jpg  https://graph.org/file/1bd6fa19297caf4189c61.jpg  ').split()
    SYD = os.environ.get("SYD", 'https://graph.org/file/3b2b8110f6f57f7fc5c74.jpg')
    ADMIN = [int(admin) if id_pattern.search(
        admin) else admin for admin in os.environ.get('ADMIN', '').split()]  # ⚠️ Required

   # FORCE_SUB = os.environ.get("FORCE_SUB", "") # ⚠️ Required Username without @
  #  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))  # ⚠️ Required
    FLOOD = int(os.environ.get("FLOOD", '10'))
    BANNED_USERS = set(int(x) for x in os.environ.get(
        "BANNED_USERS", "1234567890").split())

    # wes response configuration
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    WOOK = bool(os.environ.get("WOOK", False))
    PORT = int(os.environ.get("PORT", "8080"))


class Txt(object):
    # part of text configuration
    START_TXT = """<b>Hᴀɪ {} 👋,
I Δᴍ Aɴ Aᴅᴠᴀɴᴄᴇᴅ Aɴᴅ Yᴇᴛ Pᴏᴡᴇʀꜰᴜʟ Rᴇɴᴀᴍᴇ Bᴏᴛ.
 
Bot Is Set For Private Use Only, Only Follows Legal Methods In telegram.
To Do A Complaint, Message Us.

This Bot Only Messages Channel, Where It Has Right (Owned By Me, for private use only).

Bot Doesn't Works On Any Group, Neither Sends message to anyone ✅."""
    
    STRT_TXT = """<b>Hᴀɪ {} 👋,
ɪ ᴀᴍ ᴀ ᴠɪᴅᴇᴏ ᴛᴏ ꜱᴛɪᴄᴋᴇʀ ʙᴏᴛ ᴡʜɪᴄʜ ᴄᴀɴ ᴄᴏɴᴠᴇʀᴛ ᴠɪᴅᴇᴏꜱ, ɪᴍᴀɢᴇꜱ ᴀɴᴅ ɢɪꜰꜱ ɪɴᴛᴏ ꜱᴛɪᴄᴋᴇʀꜱ 
ᴀɴᴅ ꜱᴀᴠᴇ ɪᴛ ɪɴ ʏᴏᴜʀ ᴏᴡɴ ᴩᴀᴄᴋ 🪄

<blockquote>ꜱᴇɴᴅ ʏᴏᴜʀ ꜰɪʟᴇ ᴀɴᴅ ɪ ᴡɪʟʟ ᴄᴏɴᴠᴇʀᴛ ɪᴛ. 🧩
</b></blockquote>"""

    ABOUT_TXT = """<b>╭───────────⍟
➥ ᴍy ɴᴀᴍᴇ : {}
➥ Pʀᴏɢʀᴀᴍᴇʀ : <a href=https://t.me/SyD_Xyz>ꪑ𝘳 𝘴ꪗᦔ 🌐</a> 
➥ Fᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/BOT_cracker>B𝚘ᴛ ᑕяΔ¢к℮ґ 🎋</a>
➥ Lɪʙʀᴀʀy : <a href=https://t.me/+oej8cujHMFJhNmI9>Cᴏʟʟᴇᴄᴛɪᴏɴ...</a>
➥ Lᴀɴɢᴜᴀɢᴇ: <a href=https://t.me/+0Zi1FC4ulo8zYzVl>ʙΔᴄᴋ-Uᴩ 💦</a>
➥ Dᴀᴛᴀ Bᴀꜱᴇ: <a href=https://t.me/+3-nuV_9INIg0MDY1>Dʙ ⚡</a>
➥ ᴍʏ ꜱᴇʀᴠᴇʀ : <a href=https://t.me/Mod_Moviez_X>Tɢ 🗯️</a>
➥ ᴠᴇʀsɪᴏɴ : v1.0
╰───────────────⍟ """

    HELP_TXT = """
◽ <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ</u></b>
  
<b>•></b> /start Tʜᴇ Bᴏᴛ Aɴᴅ Sᴇɴᴅ Aɴy Pʜᴏᴛᴏ Tᴏ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟy Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /del_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Oʟᴅ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /view_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴɪʟᴇ.


<u><b><blockqoute>Jᴜꜱᴛ ꜱᴇɴᴅ ᴛʜᴇ ᴩɪᴄᴛᴜʀᴇ.. ⚡</blockqoute></u></b>

◽ <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ</u></b>

<b>•></b> /set_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Sᴇᴛ ᴀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /see_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /del_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
Exᴀᴍᴩʟᴇ:- <code> /set_caption 📕 Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}
⏰ Dᴜʀᴀᴛɪᴏɴ: {duration} </code>

◽ <b><u>Hᴏᴡ Tᴏ Rᴇɴᴀᴍᴇ A Fɪʟᴇ</u></b>
<b>•></b> Sᴇɴᴅ Aɴy Fɪʟᴇ Aɴᴅ Tyᴩᴇ Nᴇᴡ Fɪʟᴇ Nᴀᴍᴇ \nAɴᴅ Sᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ [ document, video, audio ].           

◽ <b><u>Sᴇᴛ ꜱᴜꜰꜰɪx ᴀɴᴅ ᴩʀᴇꜰɪx.</b></u>
<b>•></b> /set_prefix - Sᴇᴛ ᴩʀᴇꜰɪx(ꜰɪʀꜱᴛ ᴡᴏʀᴅ)
<b>•></b> /set_suffix - Sᴇᴛ ꜱᴜꜰꜰɪx(ʟᴀꜱᴛ ᴡᴏʀᴅ)
<b>•></b> /see_prefix - Sᴇᴇ ᴩʀᴇꜰɪx
<b>•></b> /see_suffix - Sᴇᴇ ꜱᴜꜰꜰɪx
<b>•></b> /del_prefix - Dᴇʟᴇᴛᴇ ᴩʀᴇꜰɪx
<b>•></b> /del_suffix - Dᴇʟᴇᴛᴇ ꜱᴜꜰꜰɪx

<b>⦿ Developer:</b> <a href=https://t.me/SyD_Xyz>🔅 ᴍ.ʀ Sʏᦔ 🔅</a>
"""

    SEND_METADATA = """
❪ SET CUSTOM METADATA ❫

☞ Fᴏʀ Exᴀᴍᴘʟᴇ:-

◦ <code> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="Powered By:- @Bot_Cracker" -metadata author="@Syd_Xyz" -metadata:s:s title="Subtitled By :- @Mod_Moviez_X" -metadata:s:a title="By :- @GetTGLinks" -metadata:s:v title="By:- @Bot_Cracker" </code>

📥 Fᴏʀ Hᴇʟᴘ Cᴏɴᴛᴀᴄᴛ..: @SyD_XyZ
"""

    STATS_TXT = """
╔════❰ Sᴇʀᴠᴇʀ sᴛᴀᴛS  ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼ ᴜᴩᴛɪᴍᴇ: `{0}`
║┣⪼ ᴛᴏᴛᴀʟ sᴘᴀᴄᴇ: `{1}`
║┣⪼ ᴜsᴇᴅ: `{2} ({3}%)`
║┣⪼ ꜰʀᴇᴇ: `{4}`
║┣⪼ ᴄᴘᴜ: `{5}%`
║┣⪼ ʀᴀᴍ: `{6}%`
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁۪۪        
"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰Pʀᴏɢʀεss ʙΔʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
┣⪼ 🩷 Bꪗ: @Bot_Cracker 🎋
╰━━━━━━━━━━━━━━━➣ </b>"""


from pyrogram import utils as pyroutils
pyroutils.MIN_CHAT_ID = -999999999999
pyroutils.MIN_CHANNEL_ID = -100999999999999

