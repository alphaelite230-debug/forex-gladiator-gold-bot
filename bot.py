from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

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
        [InlineKeyboardButton("📢 Forex Gladiator Channel", url=CHANNEL_LINK)],
    ]

    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown",
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "analysis":
        await query.message.reply_text(
            "🥇 *Gold Analysis*\n\n"
            "🔍 XAUUSD Professional Analysis\n"
            "📊 Timeframes: H1 / H4 / Daily\n\n"
            "⚠️ This feature will provide:\n"
            "- Market bias\n"
            "- Key levels\n"
            "- Trade scenarios\n\n"
            "🚧 Coming very soon for *Forex Gladiator* members.",
            parse_mode="Markdown",
        )

    elif query.data == "plans":
        await query.message.reply_text(
            "💎 *Subscription Plans*\n\n"
            "🆓 *Free*\n"
            "- One daily analysis\n"
            "- Delayed updates\n\n"
            "⚔️ *Pro*\n"
            "- Full gold analysis\n"
            "- Trade setups\n\n"
            "👑 *Elite*\n"
            "- VIP trades\n"
            "- Instant alerts\n\n"
            "💰 Payment: USDT (Telegram)\n"
            "📩 Subscription system coming next.",
            parse_mode="Markdown",
        )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    app.run_polling()


if __name__ == "__main__":
    main()
