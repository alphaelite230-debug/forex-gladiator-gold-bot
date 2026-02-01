import asyncio
import random
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8547968244:AAG2f_9xEqOTQnpJeKNcp0pcBSSuNJVNN6k"
CHANNEL_LINK = "https://t.me/FORE_XGLADIATOR"

# -------- AI CONTENT --------
def ai_bias():
    return random.choice(["Bullish 📈", "Bearish 📉", "Neutral ⏸"])

def ai_free():
    return (
        "🆓 *Free AI Gold Update*\n\n"
        f"🤖 Bias: {ai_bias()}\n"
        "• Volatility: Medium\n"
        "• No confirmed setup yet\n\n"
        "📚 Tip:\nTrade with the trend near key levels."
    )

# -------- DAILY LOOP --------
async def daily_loop(app: Application):
    sent_today = {"09": False, "18": False}

    while True:
        now = datetime.utcnow()
        hour = now.strftime("%H")

        if hour in sent_today and not sent_today[hour]:
            for chat_id in app.chat_data.keys():
                try:
                    await app.bot.send_message(
                        chat_id=chat_id,
                        text=ai_free(),
                        parse_mode="Markdown",
                    )

                    keyboard = [[InlineKeyboardButton("💎 Upgrade", callback_data="plans")]]
                    await app.bot.send_message(
                        chat_id=chat_id,
                        text="🔒 *Pro & Elite AI signals locked*",
                        reply_markup=InlineKeyboardMarkup(keyboard),
                        parse_mode="Markdown",
                    )
                except:
                    pass

            sent_today[hour] = True

        if hour == "00":
            sent_today = {"09": False, "18": False}

        await asyncio.sleep(60)

# -------- BOT --------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.application.chat_data[update.effective_chat.id] = True

    keyboard = [
        [InlineKeyboardButton("🥇 Gold Analysis", callback_data="analysis")],
        [InlineKeyboardButton("💎 Subscription Plans", callback_data="plans")],
        [InlineKeyboardButton("📢 Channel", url=CHANNEL_LINK)],
    ]

    await update.message.reply_text(
        "🥇 *Forex Gladiator Gold Bot*\n\n"
        "🤖 AI-Powered Gold Analysis\n\n"
        "👇 Choose:",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown",
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "analysis":
        await query.message.reply_text(
            "🔒 Advanced AI analysis available for Pro & Elite.\n\nUpgrade to unlock."
        )

    elif query.data == "plans":
        await query.message.reply_text(
            "💎 *Plans*\n\n"
            "🆓 Free – AI overview\n"
            "⚔️ Pro – 49 USDT\n"
            "👑 Elite – 79 USDT",
            parse_mode="Markdown",
        )

async def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))

    asyncio.create_task(daily_loop(app))
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
