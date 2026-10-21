import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎮 MLBB ID CHECKER\n\n"
        "UID နဲ့ Zone ID ကို ဒီပုံစံအတိုင်း ပို့ပါ:\n"
        "597556997(8378)"
    )


async def check_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    try:
        uid, zone_part = text.split("(", 1)
        zone = zone_part.split(")", 1)[0]

        if not uid.isdigit() or not zone.isdigit():
            raise ValueError

    except ValueError:
        await update.message.reply_text(
            "❌ UID နဲ့ Zone ID မှန်ကန်စွာ ထည့်ပါ။\n"
            "ဥပမာ: 597556997(8378)"
        )
        return

    await update.message.reply_text(
        f"✨ MLBB ID DETAILS ✨\n\n"
        f"👤 Name: မစစ်ဆေးရသေးပါ\n"
        f"🆔 UID: {uid}\n"
        f"🌐 Zone ID: {zone}\n"
        f"🌍 Region: မစစ်ဆေးရသေးပါ"
    )


if not TOKEN:
    raise RuntimeError("BOT_TOKEN မထည့်ရသေးပါ။")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_id))
app.run_polling()
