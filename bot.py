from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
import asyncio
from datetime import datetime

TOKEN = "8547968244:AAG2f_9xEqOTQnpJeKNcp0pcBSSuNJVNN6k"
CHANNEL = "@FORE_XGLADIATOR"
SUPPORT = "@FOREX_GLADIATOR_M"

USERS = set()
USER_LANG = {}
USER_PLAN = {}

# ===== START =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    USERS.add(chat_id)
    USER_LANG[chat_id] = "EN"
    USER_PLAN.setdefault(chat_id, "FREE")

    keyboard = [
        [
            InlineKeyboardButton("🇬🇧 English", callback_data="lang_en"),
            InlineKeyboardButton("🇸🇦 عربي", callback_data="lang_ar"),
        ]
    ]

    await update.message.reply_text(
        "🥇 Forex Gladiator Gold Bot\n\nChoose language / اختر اللغة:",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )

# ===== LANGUAGE =====
async def language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    chat_id = q.message.chat.id

    if q.data == "lang_en":
        USER_LANG[chat_id] = "EN"
        text = "🥇 *Forex Gladiator Gold Bot*\n\nChoose an option:"
        menu = main_menu_en()
    else:
        USER_LANG[chat_id] = "AR"
        text = "🥇 *بوت فوركس غلاديتور للذهب*\n\nاختر من القائمة:"
        menu = main_menu_ar()

    await q.answer()
    await q.edit_message_text(text, reply_markup=menu, parse_mode="Markdown")

# ===== MENUS =====
def main_menu_en():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📊 Gold Analysis", callback_data="analysis")],
        [InlineKeyboardButton("💳 Plans & Pricing", callback_data="plans")],
        [InlineKeyboardButton("📢 Join Channel", url="https://t.me/FORE_XGLADIATOR")],
    ])

def main_menu_ar():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📊 تحليل الذهب", callback_data="analysis")],
        [InlineKeyboardButton("💳 الخطط والأسعار", callback_data="plans")],
        [InlineKeyboardButton("📢 دخول القناة", url="https://t.me/FORE_XGLADIATOR")],
    ])

# ===== ANALYSIS =====
async def analysis(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    chat_id = q.message.chat.id
    plan = USER_PLAN.get(chat_id, "FREE")

    if plan == "FREE":
        text = (
            "🆓 *Free Gold Insight*\n\n"
            "• Market Bias: Neutral\n"
            "• Gold is consolidating\n\n"
            "🔒 Upgrade for full AI analysis"
        )
    else:
        text = (
            "📊 *AI Gold Analysis*\n\n"
            "• Bias: Bullish\n"
            "• Buy Zone: 2015 – 2020\n"
            "• TP: 2040\n"
            "• SL: 2005"
        )

    await q.answer()
    await q.edit_message_text(text, parse_mode="Markdown")

# ===== PLANS =====
async def plans(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    text = (
        "💳 *Subscription Plans*\n\n"
        "🆓 FREE\n"
        "• Daily bias\n"
        "• Educational insights\n\n"
        "⚔️ PRO – $49\n"
        "• Daily AI analysis\n"
        "• 1 AI trade/day\n\n"
        "👑 ELITE – $79\n"
        "• Advanced AI analysis\n"
        "• 2–3 AI trades/day\n\n"
        f"💬 After payment contact: {SUPPORT}"
    )

    await q.answer()
    await q.edit_message_text(text, parse_mode="Markdown")

# ===== AI MESSAGE =====
def generate_ai_message(plan):
    if plan == "FREE":
        return "🆓 Daily Gold Bias: Neutral\nStay safe & manage risk."
    if plan == "PRO":
        return "⚔️ PRO Signal:\nBuy Gold @2020\nSL 2005\nTP 2040"
    return "👑 ELITE Signals:\nBuy 2020 & 2012\nTP 2040 / 2060"

# ===== SCHEDULER LOOP =====
async def scheduler(app):
    sent_morning = False
    sent_ny = False

    while True:
        now = datetime.utcnow().hour

        if now == 9 and not sent_morning:
            for chat_id in USERS:
                await app.bot.send_message(chat_id, generate_ai_message(USER_PLAN.get(chat_id, "FREE")))
            sent_morning = True

        if now == 15 and not sent_ny:
            for chat_id in USERS:
                await app.bot.send_message(chat_id, generate_ai_message(USER_PLAN.get(chat_id, "FREE")))
            sent_ny = True

        if now != 9:
            sent_morning = False
        if now != 15:
            sent_ny = False

        await asyncio.sleep(60)

# ===== MAIN =====
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(language, pattern="^lang_"))
    app.add_handler(CallbackQueryHandler(analysis, pattern="analysis"))
    app.add_handler(CallbackQueryHandler(plans, pattern="plans"))

    app.create_task(scheduler(app))
    app.run_polling()

if __name__ == "__main__":
    main()
