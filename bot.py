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
            "📊 تحليل ذهب XAUUSD بالذكاء الاصطناعي\n"
            "⚔️ البوت الرسمي لقناة *Forex Gladiator*\n\n"
            "👇 اختر من القائمة:"
        )
        keyboard = [
            [InlineKeyboardButton("🥇 تحليل الذهب", callback_data="analysis")],
            [InlineKeyboardButton("💎 خطط الاشتراك", callback_data="plans")],
            [InlineKeyboardButton("🌐 اللغة", callback_data="lang")],
            [InlineKeyboardButton("📢 قناة فوركس غلاديتور", url=CHANNEL_LINK)],
        ]
    else:
        text = (
            "🥇 *Forex Gladiator Gold Bot*\n\n"
            "📊 AI-Powered XAUUSD (Gold) Analysis\n"
            "⚔️ Official Bot of *Forex Gladiator*\n\n"
            "👇 Choose an option:"
        )
        keyboard = [
            [InlineKeyboardButton("🥇 Gold Analysis", callback_data="analysis")],
            [InlineKeyboardButton("💎 Subscription Plans", callback_data="plans")],
            [InlineKeyboardButton("🌐 Language", callback_data="lang")],
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
    lang = get_lang(context)

    # 🌐 LANGUAGE
    if query.data == "lang":
        keyboard = [
            [InlineKeyboardButton("🇬🇧 English", callback_data="lang_en")],
            [InlineKeyboardButton("🇸🇦 عربي", callback_data="lang_ar")],
        ]
        await query.message.reply_text(
            "🌐 Choose language / اختر اللغة",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif query.data == "lang_en":
        context.user_data["lang"] = "en"
        await start(query, context)

    elif query.data == "lang_ar":
        context.user_data["lang"] = "ar"
        await start(query, context)

    # 🥇 ANALYSIS
    elif query.data == "analysis":
        if lang == "ar":
            text = (
                "🔒 *تحليل الذهب (ذكاء اصطناعي)*\n\n"
                "هذا القسم متاح فقط لمشتركي *Pro* و *Elite*.\n\n"
                "🤖 ما يقدمه الذكاء الاصطناعي:\n"
                "• اتجاه الذهب\n"
                "• مناطق دعم ومقاومة\n"
                "• أفكار صفقات ذكية\n\n"
                "👇 قم بالترقية:"
            )
        else:
            text = (
                "🔒 *Gold Analysis (AI Powered)*\n\n"
                "Available for *Pro & Elite* members only.\n\n"
                "🤖 AI provides:\n"
                "• Gold market bias\n"
                "• Key levels\n"
                "• Smart trade ideas\n\n"
                "👇 Upgrade your plan:"
            )

        keyboard = [[InlineKeyboardButton("💎 Plans", callback_data="plans")]]
        await query.message.reply_text(
            text,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown",
        )

    # 💎 PLANS
    elif query.data == "plans":
        keyboard = [
            [InlineKeyboardButton("🆓 Free", callback_data="free")],
            [InlineKeyboardButton("⚔️ Pro – 49 USDT", callback_data="pro")],
            [InlineKeyboardButton("👑 Elite – 79 USDT", callback_data="elite")],
        ]

        text = "💎 *خطط الاشتراك*" if lang == "ar" else "💎 *Subscription Plans*"
        await query.message.reply_text(
            text,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown",
        )

    # 🆓 FREE
    elif query.data == "free":
        if lang == "ar":
            text = (
                "🆓 *الخطة المجانية*\n\n"
                "✔️ نظرة عامة على الذهب\n"
                "✔️ محتوى تعليمي\n\n"
                "❌ بدون صفقات\n"
                "❌ بدون دخول وخروج\n\n"
                "🤖 كل شي آلي 100%\n"
            )
        else:
            text = (
                "🆓 *Free Plan*\n\n"
                "✔️ AI gold overview\n"
                "✔️ Educational content\n\n"
                "❌ No trade signals\n"
                "❌ No SL / TP\n\n"
                "🤖 Fully automated\n"
            )

        keyboard = [[InlineKeyboardButton("💎 Upgrade", callback_data="plans")]]
        await query.message.reply_text(
            text,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown",
        )

    # PRO / ELITE
    elif query.data in ["pro", "elite"]:
        if query.data == "pro":
            price = "49 USDT"
            plan = "Pro"
        else:
            price = "79 USDT"
            plan = "Elite"

        keyboard = [
            [InlineKeyboardButton("TRC20", callback_data=f"pay_{plan}_trc")],
            [InlineKeyboardButton("BEP20 / ERC20", callback_data=f"pay_{plan}_evm")],
        ]

        await query.message.reply_text(
            f"{plan} – {price}\n\nChoose network:",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    # PAYMENT
    elif "pay_" in query.data:
        if "trc" in query.data:
            net = "TRC20"
            addr = USDT_TRC20
        else:
            net = "BEP20 / ERC20"
            addr = USDT_EVM

        await query.message.reply_text(
            f"💳 Payment\n\nNetwork: {net}\nAddress:\n{addr}\n\n"
            f"After payment contact {SUPPORT_USER}",
        )


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()


if __name__ == "__main__":
    main()
