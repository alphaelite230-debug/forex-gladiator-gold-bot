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

    # -------- ANALYSIS --------
    if query.data == "analysis":
        await query.message.reply_text(
            "🔒 *Gold Analysis*\n\n"
            "Advanced gold analysis is available for *Pro & Elite* members only.\n\n"
            "💎 Upgrade your plan to unlock:\n"
            "• Daily gold bias\n"
            "• Key supply & demand zones\n"
            "• Smart entry points",
            parse_mode="Markdown",
        )

    # -------- PLANS --------
    elif query.data == "plans":
        keyboard = [
            [InlineKeyboardButton("🆓 Free Plan", callback_data="free")],
            [InlineKeyboardButton("⚔️ Pro – 49 USDT", callback_data="pro")],
            [InlineKeyboardButton("👑 Elite – 79 USDT", callback_data="elite")],
        ]

        await query.message.reply_text(
            "💎 *Subscription Plans*\n\nChoose your plan:",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown",
        )

    # -------- FREE --------
    elif query.data == "free":
        await query.message.reply_text(
            "🆓 *Free Plan*\n\n"
            "You will get:\n"
            "• General gold market view\n"
            "• Educational posts\n"
            "• Public updates from the channel\n\n"
            "🚫 Not included:\n"
            "• Trade signals\n"
            "• Entry / SL / TP\n"
            "• Advanced analysis\n\n"
            "📢 Join our channel:\n"
            f"{CHANNEL_LINK}",
            parse_mode="Markdown",
        )

    # -------- PRO / ELITE --------
    elif query.data in ["pro", "elite"]:
        if query.data == "pro":
            plan = "Pro"
            price = "49 USDT"
            features = (
                "⚔️ *Pro Plan – 49 USDT*\n\n"
                "Includes:\n"
                "• Daily gold analysis\n"
                "• Trade setups (Entry / SL / TP)\n"
                "• Intraday bias\n"
                "• Strong key levels\n\n"
                "❌ No VIP signals"
            )
        else:
            plan = "Elite"
            price = "79 USDT"
            features = (
                "👑 *Elite Plan – 79 USDT*\n\n"
                "Includes EVERYTHING in Pro +\n"
                "• High accuracy VIP signals\n"
                "• Scalping & swing trades\n"
                "• Market sentiment updates\n"
                "• Priority support"
            )

        keyboard = [
            [InlineKeyboardButton("TRC20", callback_data=f"pay_{plan}_trc")],
            [InlineKeyboardButton("BEP20 / ERC20", callback_data=f"pay_{plan}_evm")],
        ]

        await query.message.reply_text(
            f"{features}\n\n"
            "💳 Choose payment network:",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown",
        )

    # -------- PAYMENT --------
    elif "pay_" in query.data:
        if "trc" in query.data:
            address = USDT_TRC20
            network = "TRC20"
        else:
            address = USDT_EVM
            network = "BEP20 / ERC20"

        if "Pro" in query.data:
            price = "49 USDT"
            plan = "Pro"
        else:
            price = "79 USDT"
            plan = "Elite"

        await query.message.reply_text(
            f"💳 *{plan} Plan Payment*\n\n"
            f"💰 Amount: *{price}*\n"
            f"🔗 Network: `{network}`\n"
            f"📍 Address:\n`{address}`\n\n"
            "✅ After payment:\n"
            f"Contact {SUPPORT_USER}\n"
            "Send TXID or screenshot to activate.",
            parse_mode="Markdown",
        )


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()


if __name__ == "__main__":
    main()
