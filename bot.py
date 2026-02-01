import asyncio
import random
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = "8547968244:AAG2f_9xEqOTQnpJeKNcp0pcBSSuNJVNN6k"
CHANNEL_LINK = "https://t.me/FORE_XGLADIATOR"

# ---------- AI CONTENT ----------
def ai_bias():
    return random.choice(["Bullish 📈", "Bearish 📉", "Neutral ⏸"])

def ai_free():
    return (
        "🆓 Free AI Gold Update\n\n"
        f"🤖 Bias: {ai_bias()}\n"
        "• Volatility: Medium\n"
        "• No confirmed setup yet\n\n"
        "📌 Educational insight only"
    )

# ---------- DAILY LOOP ----------
async def daily_loop(app: Application):
    sent = {"09": False, "18": False}

    while True:
        now = datetime.utcnow()
        hour = now.strftime("%H")

        if hour in sent and not sent[hour]:
            for chat_id in app.chat_data.keys():
                try:
                    await app.bot.send_message(
                        chat_id=chat_id,
                        text=ai_free(),
                    )
                    await app.bot.send_message(
                        chat_id=chat_id,
                        text="🔒 Pro & Elite AI signals locked\n💎 Upgrade to unlock",
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton("💎 Upgrade", callback_data="plans")]]
                        ),
                    )
                except:
                    pass
            sent[hour] = True

        if hour == "00":
            sent = {"09": False, "18": False}

        await asyncio.sleep(60)

# ---------- BOT HANDLERS ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.application.chat_data[update.effective_chat.id] = True

    keyboard = [
        [InlineKeyboardButton("🥇 Gold Analysis", callback_data="analysis")],
        [InlineKeyboardButton("💎 Subscription Plans", callback_data="plans")],
        [InlineKeyboardButton("📢 Channel", url=CHANNEL_LINK)],
    ]

    await update.message.reply_text(
        "🥇 Forex Gladiator Gold Bot\n\n"
        "🤖 AI-Powered Gold Analysis\n\n"
        "👇 Choose an option:",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()

    if q.data == "analysis":
        await q.message.reply_text(
            "🔒 Advanced gold analysis is for Pro & Elite members only."
        )

    elif q.data == "plans":
        await q.message.reply_text(
            "💎 Subscription Plans\n\n"
            "🆓 Free – Daily AI overview\n"
            "⚔️ Pro – 49 USDT\n"
            "👑 Elite – 79 USDT\n\n"
            "📩 After payment contact: @FOREX_GLADIATOR_M"
        )

# ---------- STARTUP ----------
async def post_init(app: Application):
    asyncio.create_task(daily_loop(app))

def main():
    app = (
        Application.builder()
        .token(TOKEN)
        .post_init(post_init)
        .build()
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))

    app.run_polling()

if __name__ == "__main__":
    main()
