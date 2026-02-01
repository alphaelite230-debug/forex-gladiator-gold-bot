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
        text = (
            "🔒 *Gold Analysis (AI Powered)*\n\n"
            "Available for *Pro & Elite* members only.\n\n"
            "🤖 Includes:\n"
            "• Gold bias\n"
            "• Key levels\n"
            "• AI trade ideas\n\n"
            "👇 Upgrade to unlock"
            if lang == "en"
            else
            "🔒 *تحليل الذهب (ذكاء اصطناعي)*\n\n"
            "متاح فقط لمشتركي *Pro* و *Elite*.\n\n"
            "🤖 يشمل:\n"
            "• اتجاه الذهب\n"
            "• مناطق مهمة\n"
            "• أفكار صفقات\n\n"
            "👇 قم بالترقية"
        )

        keyboard = [[InlineKeyboardButton("💎 Plans", callback_data="plans")]]
        await query.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    # 💎 PLANS
    elif query.data == "plans":
        text = (
            "💎 *Subscription Plans*\n\n"
            "🆓 Free – AI market overview\n"
            "⚔️ Pro – 49 USDT (Signals + Analysis)\n"
            "👑 Elite – 79 USDT (Advanced AI setups)"
            if lang == "en"
            else
            "💎 *خطط الاشتراك*\n\n"
            "🆓 مجانية – نظرة عامة بالذكاء الاصطناعي\n"
            "⚔️ Pro – 49 USDT (تحليل + صفقات)\n"
            "👑 Elite – 79 USDT (تحليل متقدم عالي الدقة)"
        )

        keyboard = [
            [InlineKeyboardButton("🆓 Free", callback_data="free")],
            [InlineKeyboardButton("⚔️ Pro – 49 USDT", callback_data="pro")],
            [InlineKeyboardButton("👑 Elite – 79 USDT", callback_data="elite")],
        ]

        await query.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    # 🆓 FREE PLAN CONTENT
    elif query.data == "free":
        text = (
            "🆓 *Free AI Gold Update*\n\n"
            "🤖 Today's AI Insight:\n"
            "• Gold bias: Neutral\n"
            "• Market volatility: Medium\n"
            "• No clear setup yet\n\n"
            "📚 Tip:\n"
            "Wait for confirmation near key levels.\n\n"
            "❌ No trade signals"
            if lang == "en"
            else
            "🆓 *التحديث المجاني للذهب*\n\n"
            "🤖 نظرة الذكاء الاصطناعي:\n"
            "• الاتجاه: حيادي\n"
            "• التذبذب: متوسط\n"
            "• لا توجد صفقة واضحة\n\n"
            "📚 نصيحة:\n"
            "انتظر تأكيد عند المناطق المهمة.\n\n"
            "❌ بدون صفقات"
        )

        keyboard = [[InlineKeyboardButton("💎 Upgrade", callback_data="plans")]]
        await query.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    # PRO / ELITE
    elif query.data in ["pro", "elite"]:
        if query.data == "pro":
            plan = "Pro"
            price = "49 USDT"
            benefits = (
                "• AI gold bias\n• Trade signals\n• Entry / SL / TP\n• Daily analysis"
                if lang == "en"
                else
                "• اتجاه الذهب\n• صفقات\n• دخول ووقف وخروج\n• تحليل يومي"
            )
        else:
            plan = "Elite"
            price = "79 USDT"
            benefits = (
                "• Everything in Pro\n• Advanced AI setups\n• Higher accuracy signals"
                if lang == "en"
                else
                "• كل ميزات Pro\n• صفقات متقدمة\n• دقة أعلى"
            )

        keyboard = [
            [InlineKeyboardButton("TRC20", callback_data=f"pay_{plan}_trc")],
            [InlineKeyboardButton("BEP20 / ERC20", callback_data=f"pay_{plan}_evm")],
        ]

        await query.message.reply_text(
            f"💎 *{plan} – {price}*\n\n{benefits}\n\nChoose network:",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown",
        )

    # PAYMENT
    elif "pay_" in query.data:
        network = "TRC20" if "trc" in query.data else "BEP20 / ERC20"
        address = USDT_TRC20 if "trc" in query.data else USDT_EVM
        price = "49 USDT" if "Pro" in query.data else "79 USDT"

        await query.message.reply_text(
            f"💳 *Payment*\n\nPlan price: {price}\nNetwork: {network}\n\nAddress:\n`{address}`\n\n"
            f"After payment contact {SUPPORT_USER}",
            parse_mode="Markdown",
        )


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()


if __name__ == "__main__":
    main()
