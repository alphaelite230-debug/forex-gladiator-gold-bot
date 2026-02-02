from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
import logging

TOKEN = "PUT_YOUR_TOKEN_HERE"

logging.basicConfig(level=logging.INFO)

# ====== TEXTS ======
TEXTS = {
    "welcome": {
        "ar": "🔥 أهلاً بك في بوت فوركس جلادياتور 🔥\n\nاختر لغتك 👇",
        "en": "🔥 Welcome to Forex Gladiator Bot 🔥\n\nChoose your language 👇",
    },
    "plans_title": {
        "ar": "اختر الخطة المناسبة لك 👇",
        "en": "Choose the plan that suits you 👇",
    },
    "free": {
        "ar": (
            "🆓 *الخطة المجانية*\n\n"
            "✔️ تحليل عام للذهب\n"
            "✔️ تحديد الاتجاه اليومي\n"
            "✔️ محتوى تعليمي\n\n"
            "❌ بدون صفقات أو نقاط دخول"
        ),
        "en": (
            "🆓 *Free Plan*\n\n"
            "✔️ General gold analysis\n"
            "✔️ Daily trend direction\n"
            "✔️ Educational content\n\n"
            "❌ No trade entries"
        ),
    },
    "pro": {
        "ar": (
            "🥈 *خطة Pro*\n\n"
            "✔️ تحليل يومي احترافي\n"
            "✔️ دعم ومقاومة\n"
            "✔️ سيناريوهات تداول\n\n"
            "💰 السعر: 49 USDT / شهرياً"
        ),
        "en": (
            "🥈 *Pro Plan*\n\n"
            "✔️ Professional daily analysis\n"
            "✔️ Support & resistance\n"
            "✔️ Trading scenarios\n\n"
            "💰 Price: 49 USDT / month"
        ),
    },
    "elite": {
        "ar": (
            "🥇 *خطة Elite*\n\n"
            "✔️ فرص مفلترة\n"
            "✔️ دقة عالية\n"
            "✔️ تحديثات أسرع\n\n"
            "💰 السعر: 79 USDT / شهرياً"
        ),
        "en": (
            "🥇 *Elite Plan*\n\n"
            "✔️ Filtered opportunities\n"
            "✔️ High precision\n"
            "✔️ Faster updates\n\n"
            "💰 Price: 79 USDT / month"
        ),
    },
    "payment": {
        "ar": (
            "💳 *الدفع عبر USDT (TRC20)*\n\n"
            "📥 أرسل المبلغ إلى:\n"
            "`YOUR_USDT_ADDRESS`\n\n"
            "📩 ثم أرسل صورة التحويل للدعم."
        ),
        "en": (
            "💳 *Payment via USDT (TRC20)*\n\n"
            "📥 Send to:\n"
            "`YOUR_USDT_ADDRESS`\n\n"
            "📩 Then send payment proof to support."
        ),
    },
}

# ====== HANDLERS ======
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🇦🇪 عربي", callback_data="lang_ar")],
        [InlineKeyboardButton("🇬🇧 English", callback_data="lang_en")],
    ]
    await update.message.reply_text(
        TEXTS["welcome"]["ar"],
        reply_markup=InlineKeyboardMarkup(keyboard),
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data.startswith("lang_"):
        lang = data.split("_")[1]
        context.user_data["lang"] = lang

        keyboard = [
            [InlineKeyboardButton("🆓 Free", callback_data="plan_free")],
            [InlineKeyboardButton("🥈 Pro", callback_data="plan_pro")],
            [InlineKeyboardButton("🥇 Elite", callback_data="plan_elite")],
        ]

        await query.edit_message_text(
            TEXTS["plans_title"][lang],
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif data.startswith("plan_"):
        lang = context.user_data.get("lang", "en")
        plan = data.split("_")[1]

        keyboard = [[InlineKeyboardButton("🔙 Back", callback_data="back_plans")]]

        if plan in ["pro", "elite"]:
            keyboard.insert(
                0,
                [InlineKeyboardButton("💳 Pay USDT", callback_data="pay")],
            )

        await query.edit_message_text(
            TEXTS[plan][lang],
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif data == "pay":
        lang = context.user_data.get("lang", "en")
        await query.edit_message_text(
            TEXTS["payment"][lang],
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("🔙 Back", callback_data="back_plans")]]
            ),
        )

    elif data == "back_plans":
        lang = context.user_data.get("lang", "en")
        keyboard = [
            [InlineKeyboardButton("🆓 Free", callback_data="plan_free")],
            [InlineKeyboardButton("🥈 Pro", callback_data="plan_pro")],
            [InlineKeyboardButton("🥇 Elite", callback_data="plan_elite")],
        ]
        await query.edit_message_text(
            TEXTS["plans_title"][lang],
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

# ====== MAIN ======
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
