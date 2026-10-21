import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎮 MLBB ID CHECKER\n\n"
        "UID နဲ့ Zone ID ကို ဒီပုံစံအတိုင်း ပို့ပေးပါ:\n"
        "597556997(8378)"
    )


async def check_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if "(" not in text or ")" not in text:
        await update.message.reply_text(
            "❌ UID နဲ့ Zone ID ထည့်ပေးပါ။\n"
            "ဥပမာ: 597556997(8378)"
        )
        return

    try:
        uid, zone_part = text.split("(", 1)
        zone = zone_part.split(")", 1)[0]

        if not uid.isdigit() or not zone.isdigit():
            raise ValueError

    except ValueError:
        await update.message.reply_text("❌ ID မှားနေပါတယ်။")
        return

    keyboard = [[
        InlineKeyboardButton("🔵 Copy ID", callback_data=f"id_{uid}"),
        InlineKeyboardButton("🟢 Copy Server", callback_data=f"zone_{zone}")
    ]]

    await update.message.reply_text(
        f"✨ MLBB ID DETAILS ✨\n\n"
        f"👤 Name: မစစ်ဆေးရသေးပါ\n"
        f"🆔 UID: {uid}\n"
        f"🌐 Zone ID: {zone}\n"
        f"🌍 Region: မစစ်ဆေးရသေးပါ",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_id))
app.run_polling()
