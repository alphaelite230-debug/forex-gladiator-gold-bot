import random
from datetime import time
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

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

def ai_pro():
    entry = round(random.uniform(2280, 2350), 2)
    return (
        "⚔️ *Pro AI Gold Signal*\n\n"
        f"Bias: {ai_bias()}\n\n"
        f"📍 Entry: {entry}\n"
        f"🛑 SL: {entry - 15}\n"
        f"🎯 TP: {entry + 30}\n\n"
        "⚠️ Risk management required"
    )

def ai_elite():
    entry = round(random.uniform(2280, 2350), 2)
    return (
        "👑 *Elite AI Gold Setup*\n\n"
        f"Bias: {ai_bias()}\n\n"
        f"📍 Entry: {entry}\n"
        f"🛑 SL: {entry - 10}\n"
        f"🎯 TP1: {entry + 25}\n"
        f"🎯 TP2: {entry + 45}\n\n"
        "🔥 High probability setup"
    )

# -------- SCHEDULED JOB --------
async def send_daily(context: ContextTypes.DEFAULT_TYPE):
    chat_ids = context.application.chat_data.keys()

    for chat_id in chat_ids:
        try:
            await context.bot.send_message(
                chat_id=chat_id,
                text=ai_free(),
                parse_mode="Markdown",
            )

            keyboard = [[InlineKeyboardButton("💎 Upgrade", callback_data="plans")]]
            await context.bot.send_message(
                chat_id=chat_id,
                text="🔒 *Pro & Elite AI signals locked*",
                reply_markup=InlineKeyboardMarkup(keyboard),
                parse_mode="Markdown",
            )

        except:
            pass

# -------- BASIC BOT --------
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
            "⚔️ Pro – 49 USDT (Signals)\n"
            "👑 Elite – 79 USDT (Advanced AI)",
            parse_mode="Markdown",
        )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))

    # ⏰ Jobs
    app.job_queue.run_daily(send_daily, time(hour=9, minute=0))
    app.job_queue.run_daily(send_daily, time(hour=18, minute=0))

    app.run_polling()

if __name__ == "__main__":
    main()
