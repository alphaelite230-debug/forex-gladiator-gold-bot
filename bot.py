from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8547968244:AAG2f_9xEqOTQnpJeKNcp0pcBSSuNJVNN6k"
CHANNEL_NAME = "Forex Gladiator"
CHANNEL_LINK = "https://t.me/ForexGladiator"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🥇 *Forex Gladiator Gold Bot*\n\n"
        "📊 Professional XAUUSD (Gold) Analysis\n"
        "⚔️ Official Bot of *Forex Gladiator*\n\n"
        "👇 Choose an option below:\n\n"
        "— — — — —\n\n"
        "🥇 *بوت فوركس غلاديتور للذهب*\n"
        "تحليل احترافي لزوج الذهب XAUUSD\n"
        "⚔️ البوت الرسمي لقناة *Forex Gladiator*"
    )

    keyboard = [
        [InlineKeyboardButton("🥇 Gold Analysis", callback_data="analysis")],
        [InlineKeyboardButton("💎 Subscription Plans", callback_data="plans")],
        [InlineKeyboardButton("📢 Forex Gladiator Channel", url=CHANNEL_LINK)]
    ]

    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
