from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8547968244:AAG2f_9xEqOTQnpJeKNcp0pcBSSuNJVNN6k"

CHANNEL_LINK = "https://t.me/FORE_XGLADIATOR"
SUPPORT_USER = "@FOREX_GLADIATOR_M"

USDT_TRC20 = "TKQbfGFi8T9wc8Ez456hes6rRoq2Jb5vpH"
USDT_EVM = "0x0579b0f7993fdddeba62ba69b00b7c459505d044"


def get_lang(context):
    return context.user_data.get("lang", "en")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context)

    if lang == "ar":
        text = (
            "🥇 *بوت فوركس غلاديتور للذهب*\n\n"
            "📊 تحليل الذهب XAUUSD بالذكاء الاصطناعي\n"
            "⚔️ البوت الرسمي لقناة Forex Gladiator\n\n"
            "👇 اختر من القائمة:"
        )
        keyboard = [
            [InlineKeyboardButton("🥇 تحليل الذهب", callback_data="analysis")],
            [InlineKeyboardButton("🆓 الخطة المجانية", callback_data="free")],
            [InlineKeyboardButton("💎 خطط الاشتراك", callback_data="plans")],
            [InlineKeyboardButton("🌐 اللغة", callback_data="lang")],
            [InlineKeyboardButton("📢 القناة", url=CHANNEL_LINK)],
        ]
    else:
        text = (
            "🥇 *Forex Gladiator Gold Bot*\n\n"
            "📊 AI-Powered XAUUSD (Gold) Analysis\n"
            "⚔️ Official Bot of Forex Gladiator\n\n"
            "👇 Choose an option:"
        )
        keyboard = [
            [InlineKeyboardButton("🥇 Gold Analysis", callback_data="analysis")],
            [InlineKeyboardButton("🆓 Free Plan", callback_data="free")],
            [InlineKeyboardButton("💎 Subscription Plans", callback_data="plans")],
            [InlineKeyboardButton("🌐 Language", callback_data="lang")],
            [InlineKeyboardButton("📢 Channel", url=CHANNEL_LINK)],
        ]

    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown",
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = get_lang(context)

    # 🌐 LANGUAGE
    if query.data == "lang":
        keyboard = [
            [InlineKeyboardButton("🇬🇧 English", callback_data="lang_en")],
            [InlineKeyboardButton("🇸🇦 عربي", callback_data="lang_ar")],
        ]
        await query.message.reply_text("🌐 Choose language / اختر اللغة", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "lang_en":
        context.user_data["lang"] = "en"
        await start(query, context)

    elif query.data == "lang_ar":
        context.user_data["lang"] = "ar"
        await start(query, context)

    # 🥇 ANALYSIS
    elif query.data == "analysis":
        text = (
            "🔒 *تحليل الذهب المتقدم*\n\n"
            "متاح فقط لمشتركي Pro و Elite.\n\n"
            "🤖 تحليل ذكي يشمل:\n"
            "• اتجاه الذهب\n"
            "• مناطق قوية\n"
            "• أفكار صفقات\n\n"
            "👇 للترقية:"
            if lang == "ar" else
            "🔒 *Advanced Gold Analysis*\n\n"
            "Available for Pro & Elite members only.\n\n"
            "🤖 AI provides:\n"
            "• Gold bias\n"
            "• Key levels\n"
            "• Trade ideas\n\n"
            "👇 Upgrade:"
        )

        keyboard = [[InlineKeyboardButton("💎 View Plans", callback_data="plans")]]
        await query.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    # 🆓 FREE PLAN
    elif query.data == "free":
        text = (
            "🆓 *الخطة المجانية*\n\n"
            "📊 اتجاه الذهب اليوم (AI)\n"
            "🧠 تعليق ذكي مختصر\n"
            "📚 معلومة تعليمية\n\n"
            "❌ بدون صفقات\n"
            "❌ بدون دخول وخروج\n\n"
            "👇 بدك تحليل كامل؟"
            if lang == "ar" else
            "🆓 *Free Plan*\n\n"
            "📊 Daily gold direction (AI)\n"
            "🧠 Short AI comment\n"
            "📚 Educational tip\n\n"
            "❌ No trade signals\n"
            "❌ No entry / SL / TP\n\n"
            "👇 Want full access?"
        )

        keyboard = [[InlineKeyboardButton("💎 Upgrade", callback_data="plans")]]
        await query.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    # 💎 PLANS
    elif query.data == "plans":
        text = (
            "💎 *خطط الاشتراك*\n\n"
            "⚔️ Pro – 49 USDT\n"
            "• صفقات AI\n"
            "• دخول / وقف / هدف\n"
            "• تحليل يومي\n\n"
            "👑 Elite – 79 USDT\n"
            "• كل مزايا Pro\n"
            "• صفقات أقوى\n"
            "• تحليل متقدم\n\n"
            "👇 اختر الخطة:"
            if lang == "ar" else
            "💎 *Subscription Plans*\n\n"
            "⚔️ Pro – 49 USDT\n"
            "• AI trade signals\n"
            "• Entry / SL / TP\n"
            "• Daily analysis\n\n"
            "👑 Elite – 79 USDT\n"
            "• Everything in Pro\n"
            "• High accuracy setups\n"
            "• Advanced analysis\n\n"
            "👇 Choose your plan:"
        )

        keyboard = [
            [InlineKeyboardButton("⚔️ Pro – 49 USDT", callback_data="pro")],
            [InlineKeyboardButton("👑 Elite – 79 USDT", callback_data="elite")],
        ]

        await query.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    # PAYMENT
    elif query.data in ["pro", "elite"]:
        price = "49 USDT" if query.data == "pro" else "79 USDT"
        plan = "Pro" if query.data == "pro" else "Elite"

        text = (
            f"{plan} – {price}\n\nاختر شبكة الدفع:"
            if lang == "ar" else
            f"{plan} – {price}\n\nChoose payment network:"
        )

        keyboard = [
            [InlineKeyboardButton("TRC20", callback_data=f"pay_{plan}_trc")],
            [InlineKeyboardButton("BEP20 / ERC20", callback_data=f"pay_{plan}_evm")],
        ]

        await query.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

    elif "pay_" in query.data:
        net = "TRC20" if "trc" in query.data else "BEP20 / ERC20"
        addr = USDT_TRC20 if "trc" in query.data else USDT_EVM

        text = (
            f"💳 الدفع\n\nالشبكة: {net}\nالعنوان:\n{addr}\n\n"
            f"بعد الدفع تواصل مع {SUPPORT_USER}"
            if lang == "ar" else
            f"💳 Payment\n\nNetwork: {net}\nAddress:\n{addr}\n\n"
            f"After payment contact {SUPPORT_USER}"
        )

        await query.message.reply_text(text)


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()


if __name__ == "__main__":
    main()
