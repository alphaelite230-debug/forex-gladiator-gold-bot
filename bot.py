from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
import asyncio
from datetime import datetime, time

TOKEN = "8547968244:AAG2f_9xEqOTQnpJeKNcp0pcBSSuNJVNN6k"
CHANNEL = "@FORE_XGLADIATOR"
SUPPORT = "@FOREX_GLADIATOR_M"

# تخزين المستخدمين
USERS = set()
USER_LANG = {}
USER_PLAN = {}

# ====== START ======
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    USERS.add(chat_id)
    USER_LANG[chat_id] = "EN"
    USER_PLAN.setdefault(chat_id, "FREE")

    keyboard = [
        [InlineKeyboardButton("🇬🇧 English", callback_data="lang_en"),
         InlineKeyboardButton("🇸🇦 عربي", callback_data="lang_ar")]
    ]
    await update.message.reply_text(
        "🥇 Forex Gladiator Gold Bot\n\nChoose language / اختر اللغة:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# ====== LANGUAGE ======
async def language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    chat_id = query.message.chat.id

    if query.data == "lang_en":
        USER_LANG[chat_id] = "EN"
        text = (
            "🥇 *Forex Gladiator Gold Bot*\n\n"
            "Choose an option:"
        )
        keyboard = main_menu_en()
    else:
        USER_LANG[chat_id] = "AR"
        text = (
            "🥇 *بوت فوركس غلاديتور للذهب*\n\n"
            "اختر من القائمة:"
        )
        keyboard = main_menu_ar()

    await query.answer()
    await query.edit_message_text(text, reply_markup=keyboard, parse_mode="Markdown")

# ====== MENUS ======
def main_menu_en():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📊 Gold Analysis", callback_data="analysis")],
        [InlineKeyboardButton("💳 Plans & Pricing", callback_data="plans")],
        [InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/FORE_XGLADIATOR")]
    ])

def main_menu_ar():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📊 تحليل الذهب", callback_data="analysis")],
        [InlineKeyboardButton("💳 الخطط والأسعار", callback_data="plans")],
        [InlineKeyboardButton("📢 دخول القناة", url=f"https://t.me/FORE_XGLADIATOR")]
    ])

# ====== ANALYSIS BUTTON ======
async def analysis(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    chat_id = query.message.chat.id
    plan = USER_PLAN.get(chat_id, "FREE")

    if plan == "FREE":
        text = (
            "🆓 *Free Gold Overview*\n\n"
            "• Market bias: Neutral\n"
            "• Gold is ranging today\n\n"
            "🔒 Upgrade for full analysis"
        )
    else:
        text = (
            "📊 *AI Gold Analysis*\n\n"
            "• Bias: Bullish\n"
            "• Buy Zone: 2015 - 2020\n"
            "• TP: 2040\n"
            "• SL: 2005"
        )

    await query.answer()
    await query.edit_message_text(text, parse_mode="Markdown")

# ====== PLANS ======
async def plans(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    text = (
        "💳 *Subscription Plans*\n\n"
        "🆓 FREE\n"
        "• Daily bias\n"
        "• Education\n\n"
        "⚔️ PRO – $49\n"
        "• Daily analysis\n"
        "• 1 AI trade/day\n\n"
        "👑 ELITE – $79\n"
        "• Advanced analysis\n"
        "• 2–3 AI trades/day\n\n"
        f"💬 After payment contact: {SUPPORT}"
    )

    await query.answer()
    await query.edit_message_text(text, parse_mode="Markdown")

# ====== DAILY AI MESSAGE ======
def generate_ai_message(plan: str):
    if plan == "FREE":
        return "🆓 Daily Gold Bias: Neutral\nStay cautious."
    if plan == "PRO":
        return "⚔️ PRO Signal:\nBuy Gold 2020\nSL 2005\nTP 2040"
    return "👑 ELITE Signals:\nBuy 2020 / Buy 2012\nTP 2040 / 2060"

async def send_daily(context: ContextTypes.DEFAULT_TYPE):
    for chat_id in USERS:
        plan = USER_PLAN.get(chat_id, "FREE")
        try:
            await context.bot.send_message(
                chat_id=chat_id,
                text=generate_ai_message(plan)
            )
        except:
            pass

# ====== MAIN ======
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(language, pattern="^lang_"))
    app.add_handler(CallbackQueryHandler(analysis, pattern="analysis"))
    app.add_handler(CallbackQueryHandler(plans, pattern="plans"))

    # تشغيل الإرسال مرتين يوميًا
    app.job_queue.run_daily(send_daily, time(hour=9, minute=0))
    app.job_queue.run_daily(send_daily, time(hour=15, minute=0))

    app.run_polling()

if __name__ == "__main__":
    main()
