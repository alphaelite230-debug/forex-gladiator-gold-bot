from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = "PUT_YOUR_BOT_TOKEN_HERE"

# ---------- START ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["started"] = True

    keyboard = [
        [InlineKeyboardButton("🥇 Gold Analysis", callback_data="gold")],
        [InlineKeyboardButton("💎 Plans", callback_data="plans")],
        [InlineKeyboardButton("🌐 Language", callback_data="lang")],
    ]

    await update.message.reply_text(
        "🥇 Forex Gladiator Gold Bot\n\n"
        "📊 Professional XAUUSD Analysis\n\n"
        "👇 Choose an option:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# ---------- BUTTON HANDLER ----------
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "gold":
        await query.edit_message_text(
            "🔒 Gold Analysis\n\n"
            "Advanced gold analysis is available for Pro & Elite members only.\n\n"
            "💎 Upgrade your plan to unlock:\n"
            "• Daily AI gold bias\n"
            "• Smart supply & demand zones\n"
            "• AI-based entries"
        )

    elif data == "plans":
        await query.edit_message_text(
            "💎 Membership Plans\n\n"
            "🆓 Free:\n"
            "• Daily market sentiment (AI)\n\n"
            "🥈 Pro – 49$\n"
            "• Daily gold bias (AI)\n"
            "• Key zones\n\n"
            "🥇 Elite – 79$\n"
            "• Full AI analysis\n"
            "• Smart entries\n"
            "• Priority support\n\n"
            "💬 After payment contact: @FOREX_GLADIATOR_M"
        )

    elif data == "lang":
        await query.edit_message_text(
            "🌐 اختر اللغة:\n\n"
            "Arabic 🇸🇦 / English 🇺🇸\n\n"
            "(جاهزة ومفعّلة ✅)"
        )

# ---------- MAIN ----------
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
