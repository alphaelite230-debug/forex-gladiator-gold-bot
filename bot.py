from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = "8547968244:AAG2f_9xEqOTQnpJeKNcp0pcBSSuNJVNN6k"

# ===== /start =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🇸🇦 عربي", callback_data="lang_ar"),
            InlineKeyboardButton("🇺🇸 English", callback_data="lang_en"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🥇 Forex Gladiator Gold Bot\n\nاختر اللغة / Choose language 👇",
        reply_markup=reply_markup
    )

# ===== Language handler =====
async def language_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "lang_ar":
        text = (
            "🔥 أهلاً بك في بوت فوركس جلادياتور 🔥\n\n"
            "هذا البوت يقدم:\n"
            "📊 تحليلات يومية للذهب\n"
            "🤖 ذكاء اصطناعي احترافي\n\n"
            "🚀 سيتم إضافة الخطط والدفع قريباً"
        )
    else:
        text = (
            "🔥 Welcome to Forex Gladiator Bot 🔥\n\n"
            "This bot provides:\n"
            "📊 Daily gold analysis\n"
            "🤖 AI-powered insights\n\n"
            "🚀 Plans & payments coming soon"
        )

    await query.edit_message_text(text)

# ===== Main =====
def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(language_handler))

    print("🤖 Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
