# Animasi 4 file
# Created by Apis


from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.bacot(?: |$)(.*)")
async def bacot(event):
    await event.edit("**BACOT LUUU**")


@register(outgoing=True, pattern="^.sokap(?: |$)(.*)")
async def sokap(event):
    await event.edit("**SOKAP BAT JADI ORANG YA ANJING**")


@register(outgoing=True, pattern="^.woi(?: |$)(.*)")
async def woi(event):
    await event.edit("**WOI LU SEMUA**")


@register(outgoing=True, pattern="^.ngatur(?: |$)(.*)")
async def ngatur(event):
    await event.edit("**WOI ANJING , DENGER YA , JADI ORANG GAK USAH NGATUR NGATUR HIDUP ORANG YA NGENTOT , URUS AJA HIDUP LU SENDIRI BANGSAT , UDAH BENER APA KAGAK**")


@register(outgoing=True, pattern="^.berantem(?: |$)(.*)")
async def berantem(event):
    await event.edit("**WOI ANJING**")
    sleep(3)
    await event.edit("**BERANTEM YO NGENTOT**")
    sleep(3)
    await event.edit("**JANGAN JADI BANCI KETAKUTAN YA ANJING , SHARE LOCK SEKARANG BANGSAT**")
    sleep(5)
    await event.edit("**JANGAN MENTAL SOSMED DOANG LU**")


CMD_HELP.update(
    {
        "roasting": "**✘ Plugin :** `Roasting`\
        \n\n  •  **Perintah :** `.bacot`\
        \n  •  **Function : **Animasi Bacot\
        \n\n  •  **Perintah :** `.sokap`\
        \n  •  **Function : **Animasi Sokap\
        \n\n  •  **Perintah :** `.woi`\
        \n  •  **Function : **Animasi Woi\
        \n\n  •  **Perintah :** `.ngatur`\
        \n  •  **Function : **Animasi Ngatur\
        \n\n  •  **Perintah :** `.berantem`\
        \n  •  **Function : **Animasi Berantem\
    "
    }
)
