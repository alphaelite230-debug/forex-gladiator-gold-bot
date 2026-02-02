from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = "8547968244:AAG2f_9xEqOTQnpJeKNcp0pcBSSuNJVNN6k"

CHANNEL_URL = "https://t.me/FORE_XGLADIATOR"
SUPPORT_USER = "@FOREX_GLADIATOR_M"


# ====== START ======
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🇦🇪 عربي", callback_data="lang_ar"),
            InlineKeyboardButton("🇬🇧 English", callback_data="lang_en"),
        ]
    ]
    await update.message.reply_text(
        "🥇 Forex Gladiator Gold Bot\n\nاختر اللغة / Choose language 👇",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


# ====== LANGUAGE ======
async def set_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    lang = query.data
    context.user_data["lang"] = lang

    if lang == "lang_ar":
        text = (
            "🔥 أهلاً بك في بوت فوركس جلادياتور 🔥\n\n"
            "📊 تحليلات يومية للذهب XAUUSD\n"
            "🤖 مدعوم بالذكاء الاصطناعي\n\n"
            "اختر من القائمة 👇"
        )
    else:
        text = (
            "🔥 Welcome to Forex Gladiator Bot 🔥\n\n"
            "📊 Daily Gold (XAUUSD) Analysis\n"
            "🤖 AI-powered insights\n\n"
            "Choose an option 👇"
        )

    await query.edit_message_text(
        text=text,
        reply_markup=main_menu(lang),
    )


# ====== MAIN MENU ======
def main_menu(lang):
    if lang == "lang_ar":
        keyboard = [
            [InlineKeyboardButton("📊 تحليل الذهب", callback_data="gold")],
            [InlineKeyboardButton("💎 الخطط والأسعار", callback_data="plans")],
            [InlineKeyboardButton("🆓 الخطة المجانية", callback_data="free")],
            [InlineKeyboardButton("📞 الدعم", callback_data="support")],
            [InlineKeyboardButton("📢 قناتنا", url=CHANNEL_URL)],
        ]
    else:
        keyboard = [
            [InlineKeyboardButton("📊 Gold Analysis", callback_data="gold")],
            [InlineKeyboardButton("💎 Plans & Pricing", callback_data="plans")],
            [InlineKeyboardButton("🆓 Free Plan", callback_data="free")],
            [InlineKeyboardButton("📞 Support", callback_data="support")],
            [InlineKeyboardButton("📢 Our Channel", url=CHANNEL_URL)],
        ]

    return InlineKeyboardMarkup(keyboard)


# ====== BUTTON HANDLERS ======
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    lang = context.user_data.get("lang", "lang_ar")

    if query.data == "gold":
        msg = (
            "🔒 تحليل الذهب متاح فقط لمشتركي Pro و Elite\n\n"
            "💎 يشمل:\n"
            "• الاتجاه اليومي\n"
            "• مناطق عرض وطلب\n"
            "• نقاط دخول ذكية"
            if lang == "lang_ar"
            else
            "🔒 Gold analysis is for Pro & Elite members only\n\n"
            "💎 Includes:\n"
            "• Daily bias\n"
            "• Supply & demand zones\n"
            "• Smart entries"
        )

    elif query.data == "plans":
        msg = (
            "💎 الخطط:\n\n"
            "🆓 مجاني\n"
            "• تحليل خفيف\n\n"
            "🥈 Pro – 49$\n"
            "• تحليل يومي\n"
            "• صفقات\n\n"
            "🥇 Elite – 79$\n"
            "• كل شيء + أولوية"
            if lang == "lang_ar"
            else
            "💎 Plans:\n\n"
            "🆓 Free\n"
            "• Light analysis\n\n"
            "🥈 Pro – $49\n"
            "• Daily analysis\n"
            "• Trades\n\n"
            "🥇 Elite – $79\n"
            "• Everything + priority"
        )

    elif query.data == "free":
        msg = (
            "🆓 الخطة المجانية:\n\n"
            "• نظرة عامة على الذهب\n"
            "• اتجاه عام للسوق\n"
            "• بدون صفقات"
            if lang == "lang_ar"
            else
            "🆓 Free Plan:\n\n"
            "• Gold overview\n"
            "• Market bias\n"
            "• No trades"
        )

    elif query.data == "support":
        msg = (
            f"📞 للتواصل والدعم:\n{SUPPORT_USER}"
            if lang == "lang_ar"
            else
            f"📞 Support:\n{SUPPORT_USER}"
        )

    else:
        msg = "—"

    await query.edit_message_text(
        text=msg,
        reply_markup=main_menu(lang),
    )


# ====== MAIN ======
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(set_language, pattern="^lang_"))
    app.add_handler(CallbackQueryHandler(buttons))

    print("🤖 Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
