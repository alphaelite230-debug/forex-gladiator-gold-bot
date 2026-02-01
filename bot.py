import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = "8547968244:AAG2f_9xEqOTQnpJeKNcp0pcBSSuNJVNN6k"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# ===== /start =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("🇸🇦 العربية"), KeyboardButton("🇺🇸 English")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "🥇 Forex Gladiator Gold Bot\n\n"
        "اختر اللغة / Choose language 👇",
        reply_markup=reply_markup
    )

# ===== Language handler =====
async def language_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🇸🇦 العربية":
        await update.message.reply_text(
            "✅ تم اختيار العربية\n\n"
            "الخطة المجانية:\n"
            "• نظرة عامة على الذهب\n"
            "• توجه السوق اليومي\n\n"
            "اكتب: تحليل الذهب"
        )

    elif text == "🇺🇸 English":
        await update.message.reply_text(
            "✅ English selected\n\n"
            "Free Plan:\n"
            "• General gold outlook\n"
            "• Daily market bias\n\n"
            "Type: Gold Analysis"
        )

# ===== Gold analysis (free demo) =====
async def gold_analysis(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 Gold Analysis (AI Generated)\n\n"
        "• Market Bias: Bullish\n"
        "• Key Zone: 2015 - 2035\n"
        "• Note: This is a light free analysis\n\n"
        "🔒 Pro & Elite unlock full signals"
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex("تحليل الذهب|Gold Analysis"), gold_analysis))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, language_handler))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
