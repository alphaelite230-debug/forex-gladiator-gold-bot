from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = "8547968244:AAG2f_9xEqOTQnpJeKNcp0pcBSSuNJVNN6k"

CHANNEL_LINK = "https://t.me/FORE_XGLADIATOR"
SUPPORT_USER = "@FOREX_GLADIATOR_M"

USDT_TRC20 = "TKQbfGFi8T9wc8Ez456hes6rRoq2Jb5vpH"
USDT_EVM = "0x0579b0f7993fdddeba62ba69b00b7c459505d044"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🥇 *Forex Gladiator Gold Bot*\n\n"
        "📊 Professional XAUUSD (Gold) Analysis\n"
        "⚔️ Official Bot of *Forex Gladiator*\n\n"
        "👇 Choose an option below:"
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
            "🔒 *Gold Analysis*\n\n"
            "This section is available for *Pro & Elite* members only.\n\n"
            "👉 Please subscribe to unlock full analysis.",
            parse_mode="Markdown",
        )

    elif query.data == "plans":
        keyboard = [
            [InlineKeyboardButton("🆓 Free Plan", callback_data="free")],
            [InlineKeyboardButton("⚔️ Pro – 49 USDT", callback_data="pro")],
            [InlineKeyboardButton("👑 Elite – 79 USDT", callback_data="elite")],
        ]

        await query.message.reply_text(
            "💎 *Subscription Plans*\n\n"
            "Choose your plan:",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown",
        )

    elif query.data in ["pro", "elite"]:
        price = "49 USDT" if query.data == "pro" else "79 USDT"
        plan = "Pro" if query.data == "pro" else "Elite"

        keyboard = [
            [InlineKeyboardButton("TRC20", callback_data=f"pay_{plan}_trc")],
            [InlineKeyboardButton("BEP20 / ERC20", callback_data=f"pay_{plan}_evm")],
        ]

        await query.message.reply_text(
            f"💰 *{plan} Plan – {price}*\n\n"
            "Choose payment network:",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown",
        )

    elif "pay_" in query.data:
        if "trc" in query.data:
            address = USDT_TRC20
            network = "TRC20"
        else:
            address = USDT_EVM
            network = "BEP20 / ERC20"

        await query.message.reply_text(
            f"💳 *Payment Details*\n\n"
            f"🔗 Network: `{network}`\n"
            f"📍 Address:\n`{address}`\n\n"
            "✅ After payment:\n"
            f"Contact {SUPPORT_USER}\n"
            "Send TXID or screenshot to activate your subscription.",
            parse_mode="Markdown",
        )


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()


if __name__ == "__main__":
    main()
